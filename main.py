if __name__ == "__main__":
  import uvicorn
  uvicorn.run("src.ml_api.api.app:app", host="127.0.0.1", port=8000)
