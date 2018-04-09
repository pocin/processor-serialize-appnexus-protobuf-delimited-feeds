# Decompress appnexus protobuf-delimited cloudexport files
at this moment `.proto` schemas `0.1.8`

Read all files in `/data/in/files/**/*.pb`, parse with the compiled schemas and write to corresponding (folder hierarchy is kept) locations in `/data/out/files`


# Configuration
```
{
    "definition": {
        "component": "pocin.processor-appnexus-protobuf-feeds"
    }
}


```

# How to update schemas
1. Download the latest `.proto` schemas from https://wiki.appnexus.com/display/console/Batch+Log-Level+Data
2. Place the `lld-schemas*.zip` file to the root of this repo (where `Makefile` is)
3. Run

```
$ make compile-protobuf

```

## Run locally
```
docker-compose run --rm -v path/to/infiles:/data/in/files dev
```

The parsed files will be in `./data/out/files/`


## Run tests

```
make test
# after dev session is finished to clean up containers..
make clean 
```


