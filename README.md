# halal-screen-back

- Clone with submodules
  ```git clone --recursive [repository-url]```
- Update submodules
  ```git submodule update --recursive --remote```

### Compile protobuf

```bash
poetry run python -m grpc_tools.protoc -I. --python_out=. --pyi-out=. --grpc_python_out=. ./halal-screen-proto/converter_service.proto
```

## Add model for detections

See More `detection` folder