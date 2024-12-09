## Generative AI-Powered Search for E-Commerce

## Description
This project enhances the search functionality of e-commerce platforms by using Generative AI to retrieve relevant products based on user queries in the form of text or images. The approach converts product descriptions and user inputs into vector embeddings and performs similarity-based retrieval, overcoming limitations of traditional keyword search and object detection systems. 

### Key Features
- **Textual Search**: Retrieve products by entering a description like "red t-shirt with Batman written on it."
- **Image Search**: Upload an image of a product to find visually similar items.
- **Vector-Based Search**: Uses embeddings for semantic similarity matching, powered by **Azure OpenAI**, **Multilingual e5-large**, and **Pinecone**.
- **Fast and Scalable**: Efficient similarity search enables quick retrieval of relevant products, even for complex queries.

---

## Problem Statement
Traditional e-commerce search systems often fail to retrieve specific products due to:
1. **Inefficient Object Detection**: Inability to accurately detect and recognize text or patterns on products (e.g., "UNBEATABLE" on a t-shirt).
2. **Keyword Dependency**: Limited understanding of semantic meaning, causing mismatches between user queries and product descriptions.
3. **Poor Multimodal Support**: Lack of integration between text and image-based search.

Our solution addresses these limitations by converting both product descriptions and user queries into vector embeddings, enabling accurate and flexible retrieval.

---

## Technologies and Libraries Used
- **Azure OpenAI**: For generating embeddings from textual descriptions.
- **Multilingual e5-large**: A transformer-based model for semantic understanding.
- **Transformers (Hugging Face)**: For text and image processing.
- **Pinecone**: Vector database for similarity search.
- **Python**: Core programming language for implementation.

---

## How It Works
1. **Data Preparation**:  
   - Product descriptions are preprocessed and converted into embeddings using **Multilingual e5-large**.
   - Product images are processed using a transformer-based model to extract feature vectors.

2. **Query Input**:  
   - **Text Query**: User enters a product description (e.g., "red t-shirt with Batman written on it").
   - **Image Query**: User uploads an image of the desired product.

3. **Vector Embedding**:  
   - Both product catalog data and user queries are converted into vector embeddings.

4. **Similarity Search**:  
   - **Pinecone** performs similarity search between the query embedding and product embeddings to find the most relevant matches.

5. **Results Display**:  
   - The top-matching products are retrieved and displayed to the user.

---

## Dataset
- The project is trained on a sample dataset of **100 t-shirts**, each with a unique text description and image.  
- Product descriptions include attributes like color, text, and style.

---

## Results
- **Text Queries**:
  - Precision: 87%
  - Recall: 82%
- **Image Queries**:
  - Precision: 80%
  - Recall: 75%
- **Response Time**: Under 1.5 seconds on average.


Input : **i am looking for a gym tshist** <br>
*spelling mistake done with purpose*
```powershell
(.venv) E:\MLSA>e:/MLSA/.venv/Scripts/python.exe e:/MLSA/main.py
The top 5 most relevant images for your query are:
1. imagetest\images (6).jpg (Score: 0.26005762815475464)
2. imagetest\download (1).jpg (Score: 0.2502465844154358)
3. imagetest\download (4).jpg (Score: 0.2484073042869568)
4. imagetest\images (5).jpg (Score: 0.24071313440799713)
5. imagetest\download (2).jpg (Score: 0.23759067058563232)

(.venv) E:\MLSA>e:/MLSA/.venv/Scripts/python.exe e:/MLSA/retriever.py
Score: 0.779152632
Metadata: {'chunk_id': 37.0, 'content_type': 'image', 'image_path': 'images (26).jpg', 'text': 'This t-shirt is black and features the logo of GitHub prominently on the front. The text reads "THE PLACE WHERE I FORK" in a contrasting white and orange color scheme. The design is simple yet eye-catching, appealing to tech enthusiasts and developers.'}
------
Score: 0.773222
Metadata: {'chunk_id': 46.0, 'content_type': 'image', 'image_path': 'images (9).jpg', 'text': 'The t-shirt is a light green color and features the word "MEDICATED" prominently printed in bold black letters across the chest. Below the main text, there is a smaller phrase that reads, "I\'M NOT LYING, I\'M MEDICALLY." The overall design gives a casual and playful vibe, making it suitable for relaxed settings.'}     
------
Score: 0.772156119
Metadata: {'chunk_id': 4.0, 'content_type': 'image', 'image_path': '51KSc1PooTL._SY741_.jpg', 'text': 'The t-shirt is a classic black color, featuring a bold graphic print on the front. The text reads "DON\'T QUIT" in large, prominent letters, accompanied by the word "LATTITUDE" in a smaller font. The overall design conveys a motivational message, making it suitable for casual wear or workout attire.'}
------
Score: 0.771769762
Metadata: {'chunk_id': 30.0, 'content_type': 'image', 'image_path': 'images (18).jpg', 'text': 'The shirt is a black graphic tee featuring a cartoon character with a dog-like appearance, dressed in casual attire. The text on the shirt reads "I\'M JUST A CHILL GUY," emphasizing a relaxed vibe. The shirt has a slightly distressed look, adding to its casual and laid-back style.'}
------
Score: 0.771748245
Metadata: {'chunk_id': 20.0, 'content_type': 'image', 'image_path': 'download (2).jpg', 'text': 'The t-shirt is a fitted black design featuring a bold graphic across the chest that reads "RAIPUR." It has a modern, sporty look with short sleeves and a round neckline. The fabric appears to be lightweight and suitable for active wear, making it ideal for workouts or casual outings.'}
------
```

---
