import os, sys

print ("\033[1;32mSilahkan Masukkan Username & Password Anda")

print ("\033[1;32matau silahkan Hubungi 082313234485 ")

username = 'AnjingKecil'

password = 'Bangsat123'



def restart():

        ngulang = sys.executable

        os.execl(ngulang, ngulang, *sys.argv)



def main():

        uname = raw_input("username : ")

        if uname == username:

                pwd = raw_input("password : ")



                if pwd == password:

                        print "\033[1;32mAlhmdllh sudah masuk juga..",

                        sys.exit()



                else:

                        print "\033[1;32mMaaf Password Yang Anda Masukkan  Salah... [?]\033[00m"

                        print "Silahkan segera log-in kembali...!!\n"

                        restart()



        else:

                print "\033[1;32mMaaf Username Yang Anda Masukkan salah... [?]\033[00m"

                print "Silahkan segera log-in kembali...!!\n"

                restart()



try:

        main()

except KeyboardInterrupt:

        os.system('clear')

        restart()
