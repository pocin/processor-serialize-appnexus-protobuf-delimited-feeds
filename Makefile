test:
	docker-compose run --rm dev python3 -m pytest

clean:
	docker-compose down

CMD_COMPILE_PROTO="find /code/ -name '*.proto' | xargs protoc --python_out=/code/protobuf_schemas -I /code/raw_protobuf_schemas/"
compile-proto:
	rm -r lld-schemas raw_protobuf_schemas || echo "nothing to clean"
	unzip lld-schemas*.zip && mv lld-schemas/schemas raw_protobuf_schemas
	mkdir protobuf_schemas || echo "protobuf_schemas exists"
	docker-compose run \
		--rm \
		dev \
	  sh -c $(CMD_COMPILE_PROTO)
dev:
	docker-compose run --rm dev
