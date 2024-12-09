from transformers import AutoTokenizer, AutoModel
import torch, os
from pinecone import Pinecone

# Initialize Pinecone
pc = Pinecone("535f3a89-b7ec-4dc1-beaa-xxxxxxxx")  # Replace with your actual API key
index = pc.Index("chat-history")

# Load the model and tokenizer
model_name = "intfloat/multilingual-e5-large"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

# Function to get mean pooled embeddings
def get_mean_pooled_embeddings(text, tokenizer, model):
    inputs = tokenizer(text, return_tensors='pt', truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
    embeddings = outputs.last_hidden_state.mean(dim=1)
    return embeddings.squeeze(0).numpy()

# Function to query Pinecone and get the best matches
def query_pinecone(text, index, top_k=5):
    # Convert the input text to embeddings
    text_embedding = get_mean_pooled_embeddings(text, tokenizer, model)

    # Query Pinecone with the embeddings
    response = index.query(
        vector=text_embedding.tolist(),
        top_k=top_k,
        include_metadata=True,
        namespace='ns2'
    )

    # Return the best matches
    return response['matches']

# Input text
input_text = "i am looking for a gym tshist"

# Get the best matches from Pinecone
best_matches = query_pinecone(input_text, index)


context = ''
# Print the best matches
for match in best_matches:
    print(f"Score: {match['score']}")
    print(f"Metadata: {match['metadata']}")
    context += match['metadata']['text'] + '\n'
    print("------")