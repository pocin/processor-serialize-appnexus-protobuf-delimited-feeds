test:
	docker-compose run --rm dev python3 -m pytest

clean:
	docker-compose down

compile-proto:
	unzip lld-schemas*.zip && mv lld-schemas protobuf_schemas
	docker-compose run \
		--rm \
		-v `pwd`/protobuf_schemas/:/schm \
		dev \
	  sh -c 'protoc --python_out=/schm --proto_path=/schm/schemas/ /schm/schemas/*.proto'
	touch ./protobuf_schemas/__init__.py

