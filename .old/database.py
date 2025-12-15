import json
import os
import threading

dbpath = "database"

class DataBase:
    def __init__(self,filename,default_data=None):
        self.filepath=f"{dbpath}/{filename}"
        self.default_data=default_data if default_data is not None else {}
        self.lock=threading.RLock()
        self._cache=None
        self._cache_valid=False
    
    def load(self):
        with self.lock:
            if self._cache_valid:
                return self._cache
            if not os.path.exists(dbpath):
                os.mkdir(dbpath) 
            if not os.path.exists(self.filepath):
                self.save(self.default_data)
                return self.default_data
            try:
                with open(self.filepath) as file:
                    data=json.load(file)
            except json.JSONDecodeError:
                self.save(self.default_data)
                return self.default_data
            
            self._cache=data
            self._cache_valid=True
            return data
    
    def save(self,data):
        with self.lock:
            with open(self.filepath,'w',encoding="utf-8") as file:
                json.dump(data,file,indent=4,ensure_ascii=False)
            self._cache=data
            self._cache_valid=True
    
    def reset(self):
        self.save(self.default_data)
    
    def all(self):
        return self.load()
    
    def set_key(self,key,value):
        data = self.load()
        data[key]=value
        self.save(data)
       
    def get_key(self,key,default=None):
        return self.load().get(key,default)
    
    def remove_key(self,key):
        data=self.load()
        if key in data:
            del data[key]
            self.save(data)
            return True
        return False
    
    def list_add(self,key,value):
        data=self.load()
        if key not in data or not isinstance(data[key],list):
            data[key]=[]
        data[key].append(value)
        self.save(data)
    
    def list_remove(self,key,value):
        data=self.load()
        if key in data and isinstance(data[key],list):
            if value in data[key]:
                data[key].remove(value)
                self.save(data)
    
    def set_path(self,path,value):
        data=self.load()
        ref=data
        for p in path[:-1]:
            if p not in ref or not isinstance(ref[p],dict):
                ref[p]={}
            ref = ref[p]
        ref[path[-1]]=value
        self.save(data)
    
    def get_path(self,path,default=None):
        data=self.load()
        ref=data
        for p in path:
            if p not in ref:
                return default
            ref=ref[p]
        return ref
    
    def remove_path(self, path):
        data = self.load()
        ref = data
        for p in path[:-1]:
            if p not in ref or not isinstance(ref[p], dict):
                return False
            ref = ref[p]
        
        if path[-1] in ref:
            del ref[path[-1]]
            self.save(data)
            return True
        return False
    
    def list_add_path(self,path,value):
        data=self.load()
        ref=data
        for p in path[:-1]:
            if p not in ref or not isinstance(ref[p],dict):
                ref[p]={}
            ref=ref[p]
        key=path[-1]
        if key not in ref or not isinstance(ref[key],list):
            ref[key]=[]
        ref[key].append(value)
        self.save(data)
    
    def list_remove_path(self,path,value):
        data=self.load()
        ref=data
        for p in path[:-1]:
            if p not in ref or not isinstance(ref[p],dict):
                return False
            ref=ref[p]
        key=path[-1]
        if key in ref and isinstance(ref[key],list):
            if value in ref[key]:
                ref[key].remove(value)
                self.save(data)
                return True
        return False


