# Move to the root of the project, to simplify path logic.
cd ../..

# Set the variables for which coverage file to output to,
coverage_type='coverage'
coverage_file="Tests/Coverage/.${coverage_type}"
html_out="Tests/htmlcov/${coverage_type}"

# Discover any unit Tests that exist, and run them.
coverage run --data-file="${coverage_file}" -m unittest discover
coverage html --data-file="${coverage_file}" --directory="${html_out}"
exit
