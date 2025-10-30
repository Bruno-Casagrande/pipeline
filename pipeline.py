import kagglehub

# Download latest version
path = kagglehub.dataset_download("nome/projeto/pipeline/data/raw")

print("Path to dataset files:", path)