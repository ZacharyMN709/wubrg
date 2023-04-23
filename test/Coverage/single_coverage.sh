# Move to the root of the project, to simplify path logic.
cd ../..

# Get the module and file name from the arguments provided.
module_name=$1
file_name=$2

# Set the variables for which coverage file to output to,
#  and which module to display code for.
coverage_type='single'
coverage_file="test/Coverage/.${coverage_type}"
target_module="core/${module_name}/*"
html_out="test/htmlcov/${coverage_type}"

# Choose the file or module to test based on if a filename exists.
if [ -n "${file_name}" ]; then
  to_test="test.test_modules.test_${module_name}.test_${file_name}"
  test_log="test/test_modules/test_${module_name}/test_${file_name}.py"
else
  to_test="test.test_modules.test_${module_name}"
  test_log="test/test_modules/test_${module_name}/*"
fi

# Run the coverage program, only if a module was defined.
if [ -n "${module_name}" ]; then
  coverage run --data-file="${coverage_file}" -m unittest discover "${to_test}"
  # TODO: Try and isolate only the file, and not the whole module, when file is provided.
  coverage html --data-file="${coverage_file}" --include="${target_module}","${test_log}"  --directory="${html_out}"
fi

exit
