# How to creat a new package

### Create the package type the following command

```sh
ros2 pkg create --build-type ament_python py_<pkg_name>
```

Move to the `<ws>/src/py_<pkg_name/py_<pkg_name>` folder and open a new python file named `<individual_name>.py`. 

```python
# import all needed Librarys
import rclpy
import <library_name>

# handles creation of nodes --> Elternklasse/ parent class
from rclpy.node import Node

# import ros interfaces
from <interface_package>.<interface_type> import <interface_name>    # std_msgs equals standard messages

# create main class
class <class_name>(Node):           # camelcase 
    # create a class as a subclass(Node) of the class constructor to setup the node
    def __init__(self):
        # initiate the Node class's constructor and name it
        super().__init__('<name>')  # splitcase
        

        # create the publisher | this will publish a String to the addison topic
        self.<publisher_name> = self.create_publisher(String, 'addison', 10)  
        # (msg.type, topic, queue size as integer)
        # dialog talker


    def <function name>(self):
     

def main(args=None):

    # initiate rclpy library
    rclpy.init(args=args)

    # initiate object of node class
    <object_name> = <class_name>()

    # running node
    rclpy.spin(<object_name>)
    
    # stops node
    <object_name>.destroy_node()

    # clears memory
    rclpy.shutdown()

# if name of the pkg equals name of the main_part
if __name__ == "__main__":
    main()
```

After you've created the code you must let your system know it. Open the `package.xml` file. Now, between `<license>` and the first `<test_depend>` tags, add the two dependencies your node needs in order to compile, if they are not included.

```
<exec_depend>rclpy</exec_depend>
<exec_depend><interface_packages></exec_depend>
```

The second line needs to be included for every package.

Save the file.

Edit the Setup.py within the entry_points like the following code.

```
entry_points={
        'console_scripts': [
                '<node_name>= <package_name>.<file_name>:main',
        ],
},
```

Afterwards you must compile the package. Execute the `colcon build` command in the workspace directory.

```
colcon build --packages-select <package_name>
```