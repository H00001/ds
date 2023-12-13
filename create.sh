#!/bin/bash
CURRENT_DIR=$(cd $(dirname $0); pwd)
if test -f output_*.md; then
	rm output_*.md
fi

for i in {1..11};do 
	cat ${i}.md >> output_0.md
done

python3 ./script/add_index.py ${CURRENT_DIR}/output_0.md ${CURRENT_DIR}/output_1.md 
rm output_0.md

cat  h-0.md copyright.md h-1.md id.md 0.md output_1.md l-1.md l-2.md > index.md

if test -f output_*.md; then
	rm output_*.md
fi

echo 'file index.md has been created'
