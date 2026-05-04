# Variables
ANTLR=antlr4
GRAMMAR=forth.g4
OUTPUT_DIR=.
PYTHON_FILES=forthLexer.py forthParser.py forthVisitor.py

# Default target
all: $(PYTHON_FILES)
# Generate Python files from the grammar
$(PYTHON_FILES): $(GRAMMAR)
	$(ANTLR) -Dlanguage=Python3 -visitor -no-listener -o $(OUTPUT_DIR) $(GRAMMAR)
# Clean up generated files
clean:
	rm -f forthLexer.py forthParser.py forthVisitor.py forth.tokens forth.interp forthLexer.interp forthLexer.tokens
# Run the interpreter
run:
	python3 -i forth.py

test:
	python3 -m doctest test.txt