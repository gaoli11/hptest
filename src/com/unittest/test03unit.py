#coding=utf-8
import copy

class globalvar():
    classrec = {} # 初始化空字典，将一条记录的id，name,li,le,ts等实体信息存放到字典
    classdat = [] # 初始化空列表，将所有记录存放到列表

    def set_name(self, ids, classname, li, le, ts):
        self.classrec['id'] = ids
        self.classrec['name'] = classname
        self.classrec['li'] = li
        self.classrec['le'] = le
        self.classrec['ts'] = ts
        self.classdat.append(copy.deepcopy(self.classrec))# 将字典作为一个元素添加到列表

    def get_name(self):
        return self.classdat[-1]

    def get_names(self):
        return self.classdat

    def get_rec(self):
        return self.classrec

if __name__ == '__main__':
    ran, name, li, le, sysdate = (2324, 'hailan', 2, 3, '2015-11-18')
    ran1, name1, li1, le1, sysdate1 = (232422, 'deppon', 3, 5, '2016-11-18')
    gl = globalvar()
    gl.set_name(ran, name, li, le, sysdate)
    gl.set_name(ran1, name1, li1, le1, sysdate1)
    print(gl.get_names())
    print(gl.get_rec())

#     
#     gl1 = globalvar()
#     gl2 = globalvar()
#     #     print(gl.get_name())
#     print(gl1.get_name())
#     print(gl2.get_name())
#     print(gl1.get_names())
#     print(gl1.get_rec())
