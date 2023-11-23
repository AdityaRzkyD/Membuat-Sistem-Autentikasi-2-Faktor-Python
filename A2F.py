import pyotp
import qrcode

NewUsername = ""
NewPassword = ""
Email = ""
Condition = True

while Condition == True:
    print("Menu Login\n1. SignIn\n2. SignUp\n")

    pil = input("Masukkan Pilihan(1-2) : ")

    Back = ""

    if pil == "2":
        NewUsername = input("Masukkan Username Baru : ")
        NewPassword = input("Masukkan Password Baru : ")
        Email = input("Masukkan Email : ")
        print("\nAkun Telah Terdaftar")
        Back = input("\nTekan Enter untuk kembali ke menu login ")
        Condition == True
    elif pil == "1":
        Kondisi = True
        while Kondisi == True:
            Username = input("Username : ")
            Password = input("Password : ")
            if Username == NewUsername and Password == NewPassword:
                print("Kode telah terkirim ke "+Email)
        
                key = "KelompokSatuKemsisInformatika"

                url = pyotp.totp.TOTP(key).provisioning_uri(name="KelompokSatuC",
                                                    issuer_name="ProjectUTS Kemsis")

                qrcode.make(url).save("totp.png")

                totp = pyotp.TOTP(key)

                Code = True
                while Code == True:
                    Input_Code = input("Enter Code : ")

                    if totp.verify(Input_Code) == True:
                        Code = False
                        Kondisi = False
                        Condition = False
                    else:
                        print("Kode yang anda masukkan salah")
                        Code = True
            else:
                print("Username atau Password salah")
                Kondisi = True
    else:
        print("Tidak ada opsi pilihan yang anda masukkan")
        Condition = True

print("Login Berhasil")