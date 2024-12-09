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

---
