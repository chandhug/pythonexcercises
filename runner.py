import main as main
import jtl_reader as jmeterlogs


def python_exercises():
    main.read_xml_using_elementtree(1, 2)
    main.replace_json_element(['inParams', 'outParams'], 'appdate')
    jmeterlogs.read_jtl_with_csv()


if __name__ == "__main__":
    print("-"*50)
    print("   Running tests     ")
    print("-"*50)
    python_exercises()