# knowledge-base-api

Senior Software Engineer Home Assignment. 




## Comments

- The structure is somewhat excessive for such a small application, but I believe it allows for more testiblity and less effort to add features (if it was a production service)
- .
- The provided model resulted in seg fault when trying to calculate embeddings, which I did not have time to debug. Hence, I wrote FakeTransformer, I believe it will suffice for the purpose of HA.
    ```python3
    # /app/transformers/fake.py
    
    class FakeTransformer:
        def __init__(self, dimension: int = 50):
            self.dimension = dimension
    
        def encode(self, s) -> List[float]:
            return [random.random() for _ in range(self.dimension)]
    ```
  
## Running 

Run in docker for development
```shell
make build
make run 
```


