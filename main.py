import os    
import torch    
from PIL import Image    
from torchvision import transforms    
from transformers import CLIPProcessor, CLIPModel    
    
def load_clip_model():    
    # Load the CLIP model and processor    
    model = CLIPModel.from_pretrained("openai/clip-vit-base-patch16")    
    processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch16")    
    return model, processor    
    
def preprocess_images(image_folder):    
    # Collect all image paths and open images as PIL objects    
    image_paths = [os.path.join(image_folder, img) for img in os.listdir(image_folder) if img.lower().endswith(('png', 'jpg', 'jpeg', 'gif', 'bmp'))]    
    images = [Image.open(image_path).convert("RGB") for image_path in image_paths]    
    return images, image_paths    
    
def search_images(query, images, image_paths, model, processor):    
    # Preprocess images    
    image_inputs = processor(images=images, return_tensors="pt", padding=True)    
    # Preprocess text    
    text_inputs = processor(text=[query], return_tensors="pt", padding=True)    
    
    # Get image and text embeddings    
    with torch.no_grad():    
        image_features = model.get_image_features(**image_inputs)    
        text_features = model.get_text_features(**text_inputs)    
        
    # Normalize the features    
    image_features = image_features / image_features.norm(p=2, dim=-1, keepdim=True)    
    text_features = text_features / text_features.norm(p=2, dim=-1, keepdim=True)    
    
    # Compute the similarity between text and images    
    similarities = (image_features @ text_features.T).squeeze()  # shape: (num_images,)    
    
    # Find the indices of the images with the highest similarity scores    
    top_k = min(5, len(images))  # Number of top matches to return    
    top_k_scores, top_k_indices = torch.topk(similarities, top_k)    
    # Get the corresponding image paths    
    top_k_indices = top_k_indices.squeeze().tolist()  # Convert indices to list    
    if isinstance(top_k_indices, int):  # If only one image    
        top_k_indices = [top_k_indices]    
    top_k_image_paths = [image_paths[i] for i in top_k_indices]    
    # Return top_k image paths and their scores    
    return top_k_image_paths, top_k_scores.tolist()    
    
def main(image_folder, query):    
    # Load CLIP model and processor    
    model, processor = load_clip_model()    
    
    # Preprocess images    
    images, image_paths = preprocess_images(image_folder)    
    
    # Find the most relevant images    
    top_k_image_paths, top_k_scores = search_images(query, images, image_paths, model, processor)    
    print(f"The top {len(top_k_image_paths)} most relevant images for your query are:")    
    for idx, (img_path, score) in enumerate(zip(top_k_image_paths, top_k_scores)):    
        print(f"{idx+1}. {img_path} (Score: {score})")    
    
# Entry point of the script    
if __name__ == "__main__":    
    image_folder = "imagetest"  # Folder containing the images    
    query = "i am looking for a gym tshist"  # Replace with your query    
    main(image_folder, query)  