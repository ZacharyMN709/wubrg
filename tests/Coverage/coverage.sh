# Move to the root of the project, to simplify path logic.
cd ../..

# Set the variables for which coverage file to output to,
coverage_type='coverage'
coverage_file="tests/Coverage/.${coverage_type}"
html_out="tests/htmlcov/${coverage_type}"

# Discover any uni tests that exist, and run them.
coverage run --data-file="${coverage_file}" -m unittest discover
coverage html --data-file="${coverage_file}" --directory="${html_out}"
exit
