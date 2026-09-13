from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(
    file_path = "../test/Neural-Networks.pdf"
)
docs = loader.load()

print("Number of pages:", len(docs))
print(docs)

print("\nFirst page:")
print(docs[0].page_content)
# print("\nMetadata:")
# print(docs[0].metadata)
