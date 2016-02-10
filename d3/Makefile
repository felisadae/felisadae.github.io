GENERATED_FILES = \
	unemployment.tsv

.PHONY: all clean

all: $(GENERATED_FILES)

clean:
	rm -rf -- $(GENERATED_FILES)

# http://www.bls.gov/lau/metrossa.htm
build/ssamatab2.txt:
	mkdir -p build
	curl -o $@ 'http://www.bls.gov/lau/ssamatab2.txt'

unemployment.tsv: process-data build/ssamatab2.txt
	./process-data build/ssamatab2.txt > $@