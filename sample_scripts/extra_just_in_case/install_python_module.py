import pip._internal
module_name_to_install = "numpy"
pip._internal.main(["install", "--target=libs", module_name_to_install])
