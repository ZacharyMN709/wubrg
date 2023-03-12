# Move to the root of the project, to simplify path logic.
cd ../..

# Get the module and file name from the arguments provided.
module_name=$1
file_name=$2

# Set the variables for which coverage file to output to,
#  and which module to display code for.
coverage_type='single'
coverage_file="Tests/Coverage/.${coverage_type}"
target_module="core/${module_name}/*"
html_out="Tests/htmlcov/${coverage_type}"

# Choose the file or module to test based on if a filename exists.
if [ -n "${file_name}" ]; then
  to_test="Tests/test_modules/${module_name}_test/${file_name}_test.py"
  test_log="Tests/test_modules/${module_name}_test/${file_name}_test.py"
else
  to_test="Tests/test_modules/${module_name}_test/__init__.py"
  test_log="Tests/test_modules/${module_name}_test/*"
fi

# Run the coverage program, only if a module was defined.
if [ -n "${module_name}" ]; then
  coverage run --data-file="${coverage_file}" -m unittest "${to_test}"
  # TODO: Try and isolate only the file, and not the whole module, when file is provided.
  coverage html --data-file="${coverage_file}" --include="${target_module}","${test_log}"  --directory="${html_out}"
fi

exit
