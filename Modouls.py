import os
class ToDoList:
    colection = dict()
    def __init__(self):
        pass

    # -- load info -- #
    def load_info(self) -> None:
        ToDoList.colection.clear()
        lsplited_list = list()
        index = 0
        try:
            with open("./info.txt" ,'r') as fou:
                for line in fou.readlines():
                    splited_list = line.split(",")
        except:
            raise FileExistsError("I Can Not Open The File....")
        else:
            splited_list.pop()
            for num in range(0,len(splited_list),2):
                ToDoList.colection.update({splited_list[num] : splited_list[num + 1]})
        

    # -- Add Item -- #
    def add_item(self,key:str,value:str) -> None:
        try:
            with open("./info.txt" , '+a') as fin:
                fin.write(f"{key}")
                fin.write(f",{value},")
        except:
            raise FileExistsError("I Can Not open The File....")
        else:
            pass
        

    
    # -- find_item -- #
    def find_item(self,key:str) -> str:
        self.load_info()
        try:
            return ToDoList.colection[key]
        except KeyError:
            raise KeyError(f"{key} Not Found....")
    
    # -- remove item -- #
    def remove_item(self,key:str) -> None:
        self.load_info()
        try:
            ToDoList.colection.pop(key)
        except KeyError:
            raise KeyError(f"{key} Not Found....")
        try:
            with open("./info.txt" , 'w') as fou:
                try:
                    for item in ToDoList.colection.items():
                        self.add_item(item[0],item[1])
                except:
                    pass
        except:
            raise FileExistsError("I Can Not Open The File....")
        
    def clear_screen(self) -> None:
        os.system('clear')
