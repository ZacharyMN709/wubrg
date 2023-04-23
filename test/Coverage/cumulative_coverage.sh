# Move to the root of the project, to simplify path logic.
cd ../..

# Get the module names to run coverage for.
module_names=( "$@" )

# Set the variable for which coverage file to output to.
coverage_type='cumulative'
coverage_file="test/Coverage/.${coverage_type}"
html_out="test/htmlcov/${coverage_type}"

# For each module provided, set the correct test file and run coverage.
#  If no modules are provided, this step is inherently skipped.
for module in "${module_names[@]}"
do
  test_module="test.test_modules.test_${module}"
  coverage run -a --data-file="${coverage_file}" -m unittest discover "${test_module}"
done

# Output the coverage information to html.
coverage html --data-file="${coverage_file}" --directory="${html_out}"

exit
