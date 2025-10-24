#SinglyLinkedList
#Repo: SinglyLinkedList_0002
class Node:
    def __init__(self):
        self.Data = 0
        self.Next = None

#Set start to none
START = None

def addNode():
    global START
    newNode = Node() #Sgtep 1
    nim = int(input("Masukkan NIM: ")) #Step 2.a
    newNode.Data = nim #Step 2.b

    #menambahkan di awal node 
    if START is None or nim <= START.Data: #Step 3
        if START  is not None and nim == START.Data: #Step 3.a
            print("NIM Sudah ada")#Step 3.a
            return
        
        newNode.next = START #Step 3.b
        START = newNode #Step 3.c
        return
    
    #Menyiapkan traversal untuk mencari  posisi pemyisipan
    previous = START #Step 4
    current = START #Step 5

    #Membaca data untuk mencari posisi penyisipan
    while (current is not None) and (nim >= current.Data): #Step r
        if nim == current.Data: #6.a
            print("NIM Sudah ada")
            return
        
        previous = current #Step 6.b
        current= current.next #Step 6.c

        #insert Node beetween two node
        newNode.next = current #step 7
        previous.next = newNode #Step 8


def serachNode (nim,current,previous):
    global START
    previous = START 
    current = START
    while current is not None and nim > current.Data:
        previous = current
        current = current.next

    if current is None:
        return False
    elif current.Data == nim:
        return True
    else:
        return False


def deleteNode(nim):
    global START 
    current = START
    previous = START 
    if serachNode(nim,previous,current) == False:
        return False
    previous.next = current.next 
    if current == START:
        START = current.next 
        return True 
    

def listEmpty():
    if START is None:
        return True
    else:
        return False
    
def traverse():
    if listEmpty():
        print("List kosong")
        input ("Tekan enter untuk lanjut...")
        return
    else:
        currentNode = START 
        while currentNode is not None:
            print("Nim:", currentNode.Data)
            currentNode = currentNode.next


def searchData():
    if listEmpty():
        print("List Kosong")
        input("Tekan Enter untuk lanjut...")
        return
    else:
        nim = int(input("Masukkan NIM: "))
        currentNode = START
        while currentNode is not None:
            if currentNode.Data == nim:
                print("NIM:", currentNode.Data)
                return
            currentNode = currentNode.next
        print("Data tidak ditemukan")


def main():
    global START
    pilihan = 0
    while pilihan != 5:
        try:
            print("1. Tambah Data")
            print("2. Hapus Data")
            print("3. Tampilkan Data")
            print("4. Cari Data")
            print("5. Keluar")
            pilihan = int(input("Pilihan: "))
            if pilihan == 1:
                addNode()
                print("Data Berhasil Ditambahkan")
                input("Tekan Enter untuk lanjut...")
            elif pilihan == 2:
                if listEmpty():
                    print("List kosong")
                    input("Tekan Enter untuk lanjut...")
                    continue

                nim = int(input("Masukkan NIM: "))
                if deleteNode(nim):
                    print("nim:", nim, "berhasil dihapus")
                    input("Tekan Enter untuk lanjut...")
                else:
                    print("Data tidak ditemukan")
            elif pilihan == 3:
                traverse()
            elif pilihan == 4:
                searchData()
            elif pilihan == 5:
                break
            else:
                print("Pilihan tidak ada")
        except Exception:
            print("Terjadi kesalahan")


if __name__ == "__main__":
    main()
    #membaca data dari yang terkecil ke terbesar