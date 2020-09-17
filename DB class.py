import sqlite3

from libs.db.dba import getConn

class db:
    conn = getConn('C:/Users/bit/Desktop/새 폴더/phon.db')
    cur = conn.cursor()
    def createtable(self):
        db.cur.execute('create table tel(name text, no text)')
    def inserttable(self,name,no):
        self.ist_sql = 'insert into tel values(?,?)'
        db.cur.execute(self.ist_sql, (name, no))
    def selecttable(self):
        self.sel_sql = 'select * from tel'
        db.cur.execute(self.sel_sql)
        rs = db.cur.fetchall()
        print('==출력결과==')
        for k,v in rs:
            print(k,v)
    def updatetable(self, n_name,o_name, n_no,o_no):
        self.upt_sql = 'update tel set name=? where name=?'
        db.cur.execute(self.upt_sql, (o_name,n_name,))
        self.upt_sql2 = 'update tel set no=? where no=?'
        db.cur.execute(self.upt_sql2, ( o_no,n_no,))
    def deletetable(self,del_name):
        self.del_sql = 'delete from tel where name==?'
        db.cur.execute(self.del_sql, (del_name,))

def main():
    tt= db() # 실제 디비를 위한 인스턴스를 생성
    while 1:
        n = input("a.테이블생성\t1.입력\t2.조회\t3.수정\t4.삭제\t0.종료\n")
        if n == "a":
            tt.createtable()
            print("새로운 저장공간이 만들어졌습니다")
        elif n == "1":
            tt.inserttable(input("name : "),input("no : "))
            print("생성이 완료되었습니다")
        elif n == "2":
            tt.selecttable()
            print("작성하신 목록입니다")
        elif n == "3":
            tt.updatetable(input("수정할 이름을 입력하세요 : "),input("수정될 이름을 입력하세요 : "),
                           input("수정할번호를 입력하세요 : "),input("수정될번호를 이름을 입력하세요 : "),)
            print("수정이 완료되었습니다")
        elif n == "4":
            tt.deletetable(input("지울사람의 이름을 입력하세요 : "))
            print("삭제가 완료되었습니다")
        elif n == "0":
            print("모든작업이 완료되었습니다\n프로그램을 종료합니다")
            tt.conn.commit()
            tt.conn.close()
            break
        else:
            continue


if __name__=="__main__":
    main()