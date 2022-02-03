import dropbox

class TransferData:
    def _init_(self,access_token):
        self.access_token=access_token
    def upload_file(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)
        with open(file_from,'rb')as f:
            dbx.files_upload(f.read(),file_to)
def main():
    access_token='sl.BBVIhrWFVFkkjZpRZH7Rywg4V2ClT-szzERska7hJoH6pg_3D4ZlvGYmGflGVPst8eqs6Gcj6Fg-JPLXV3ytMaDJ_br_salwfQPgqx6OVk5s1FwKab5yXd6oeUXtKbGVDnWefRBM0eM'
    transferData=TransferData(access_token)
    file_from=input("Enter the file path to transfer:-")
    file_to=input("Enter the full path to upload to dropbox:-")
    transferData.upload_file(file_from,file_to)
    print('file has been transfered')        
main()