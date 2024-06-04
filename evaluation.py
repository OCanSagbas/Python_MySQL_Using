import mysql.connector
import os
from bookdb import BOOKDB
from queryresult import QueryResult
from fileoperations import FileOperations

user = "deneme"  # Your userName
password = "p_deneme"  # Your password
host = "localhost"  # host name
database = "world"  # Your database name
port = 3306  # port


curentDirectory=os.getcwd()
outputDirectory = "output"
dataDirectory = "data"




def addInputTitle(title, text):
    return text + f"*** {title} ***\n"


def printException(ex):
    print(ex, "\n")

def addLine(result, text):
    return text + f"{result}\n"

def addDivider(text):
    return text + "--------------------------------------------------------------\n"

def writeBuffer(text,file):
    directory_path = os.path.join(curentDirectory, outputDirectory)
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
    file_path = os.path.join(directory_path, file)
    with open(file_path,"w") as outFile:
        outFile.write(text)
        return ""

def main():
    numberofInsertions = 0
    numberofTablesCreated = 0
    numberofTablesDropped = 0

    

    output_message = None

    bookDB = None

    dumpAuthor = "dump_author.txt"
    dumpPublisher = "dump_publisher.txt"
    dumpBook = "dump_book.txt"
    dumpAuthor_of = "dump_author_of.txt"

    try:
        bookDB = BOOKDB(user,password,host,database,port)
        bookDB.initialize()
        outputFileName="Output_{i}.txt"
        currentCounter = 0
        #####################     Dropping the database tables   #####################        
    
        numberofTablesDropped = 0

        try:
            numberofTablesDropped = bookDB.dropTables()
        except Exception as e:
            printException(e)

        output_message= addDivider("")
        output_message=addInputTitle("Drop tables", output_message)
        output_message = addLine(f"Dropped {numberofTablesDropped} tables.", output_message)
        output_message = addDivider(output_message)
        output_message = writeBuffer(output_message,outputFileName.format(i=currentCounter))

        #####################     Creating the database tables   #####################
        currentCounter += 1
        output_message=addDivider(output_message)
        output_message=addInputTitle("Create tables", output_message)
        numberofTablesCreated = 0

        try:
            numberofTablesCreated = bookDB.createTables()
            output_message= addLine(f"Created {numberofTablesCreated} tables.", output_message)
        except Exception as e:
            output_message = addLine(f"Q3.1: Exception occured:\n\n{e}", output_message)

        output_message= addDivider(output_message)
        output_message = writeBuffer(output_message,outputFileName.format(i=currentCounter))

        #####################     Inserting data into tables   #####################
        currentCounter += 1
        output_message= addDivider("")
        output_message=addInputTitle("Insert into Author", output_message)
        numberofInsertions=0
        authors=FileOperations.read_author_file(os.path.join(curentDirectory,dataDirectory,dumpAuthor))
        numberofInsertions = bookDB.insertAuthor(authors)
        output_message= addLine(f"{numberofInsertions} authors are inserted.",output_message)
        output_message = addDivider(output_message)
        output_message = writeBuffer(output_message,outputFileName.format(i=currentCounter))

        currentCounter += 1
        output_message= addDivider("")
        output_message=addInputTitle("Insert into Publisher", output_message)
        numberofInsertions=0
        publishers=FileOperations.read_publisher_file(os.path.join(curentDirectory,dataDirectory,dumpPublisher))
        numberofInsertions = bookDB.insertPublisher(publishers)
        output_message= addLine(f"{numberofInsertions} publishers are inserted.",output_message)
        output_message = addDivider(output_message)
        output_message = writeBuffer(output_message,outputFileName.format(i=currentCounter))        

        currentCounter += 1
        output_message= addDivider("")
        output_message=addInputTitle("Insert into Book", output_message)
        numberofInsertions=0
        books=FileOperations.read_book_file(os.path.join(curentDirectory,dataDirectory,dumpBook))
        numberofInsertions = bookDB.insertBook(books)
        output_message= addLine(f"{numberofInsertions} books are inserted.",output_message)
        output_message = addDivider(output_message)
        output_message = writeBuffer(output_message,outputFileName.format(i=currentCounter))       

        currentCounter += 1
        output_message= addDivider("")
        output_message=addInputTitle("Insert into Author_Of", output_message)
        numberofInsertions=0
        author_ofs=FileOperations.read_author_of_file(os.path.join(curentDirectory,dataDirectory,dumpAuthor_of))
        numberofInsertions = bookDB.insertAuthor_of(author_ofs)
        output_message= addLine(f"{numberofInsertions}  Author_ofs are inserted.",output_message)
        output_message = addDivider(output_message)
        output_message = writeBuffer(output_message,outputFileName.format(i=currentCounter))   

        #####################     Q1    #####################
        currentCounter += 1
        output_message= addDivider("")
        output_message=addInputTitle("Q1", output_message)
        
        try:
            q1Array = bookDB.functionQ1()

            # Header Line
            output_message=addLine("isbn\tfirst_publish_year\tpage_count\tpublisher_name",output_message)

            if q1Array is not None:
                for res in q1Array:
                    output_message=addLine(res,output_message)

        except Exception as e:
            output_message=addLine("Q1: Exception occurred:\n\n" + str(e), output_message)        

        output_message = addDivider(output_message)
        output_message = writeBuffer(output_message,outputFileName.format(i=currentCounter)) 

        #####################     Q2    #####################
        currentCounter += 1
        output_message= addDivider("")
        output_message=addInputTitle("Q2", output_message)
        
        try:
            q2Array = bookDB.functionQ2(14187, 29350)

            # Header Line
            output_message=addLine("publisher_id\taverage_page_count",output_message)

            if q2Array is not None:
                for res in q2Array:
                    output_message=addLine(res,output_message)

        except Exception as e:
            output_message=addLine("Q2: Exception occurred:\n\n" + str(e),output_message)     

        output_message = addDivider(output_message)
        output_message = writeBuffer(output_message,outputFileName.format(i=currentCounter))   


        #####################     Q3    #####################
        currentCounter += 1
        output_message= addDivider("")
        output_message=addInputTitle("Q3", output_message)
        
        try:
            q3Array = bookDB.functionQ3("Sue Donaldson")

            # Header Line
            output_message=addLine("book_name\tcategory\tfirst_publish_year",output_message)

            if q3Array is not None:
                for res in q3Array:
                    output_message=addLine(res,output_message)

        except Exception as e:
            output_message=addLine("Q3: Exception occurred:\n\n" + str(e),output_message)     

        output_message = addDivider(output_message)
        output_message = writeBuffer(output_message,outputFileName.format(i=currentCounter)) 


        #####################     Q4    #####################
        currentCounter += 1
        output_message= addDivider("")
        output_message=addInputTitle("Q4", output_message)
        
        try:
            q4Array = bookDB.functionQ4()

            # Header Line
            output_message=addLine("publisher_id\tcategory",output_message)

            if q4Array is not None:
                for res in q4Array:
                    output_message=addLine(res,output_message)

        except Exception as e:
            output_message=addLine("Q4: Exception occurred:\n\n" + str(e),output_message)       

        output_message = addDivider(output_message)
        output_message = writeBuffer(output_message,outputFileName.format(i=currentCounter)) 

        #####################     Q5    #####################
        currentCounter += 1
        output_message= addDivider("")
        output_message=addInputTitle("Q5", output_message)
        
        try:
            q5Array = bookDB.functionQ5(11151)

            # Header Line
            output_message=addLine("author_id\tauthor_name",output_message)

            if q5Array is not None:
                for res in q5Array:
                    output_message=addLine(res,output_message)

        except Exception as e:
            output_message=addLine("Q5: Exception occurred:\n\n" + str(e),output_message)       

        output_message = addDivider(output_message)
        output_message = writeBuffer(output_message,outputFileName.format(i=currentCounter)) 

        #####################     Q6    #####################
        currentCounter += 1
        output_message= addDivider("")
        output_message=addInputTitle("Q6", output_message)
        
        try:
            q6Array = bookDB.functionQ6()

            # Header Line
            output_message=addLine("author_id\tisbn",output_message)

            if q6Array is not None:
                for res in q6Array:
                    output_message=addLine(res,output_message)

        except Exception as e:
            output_message=addLine("Q6: Exception occurred:\n\n" + str(e),output_message)      

        output_message = addDivider(output_message)
        output_message = writeBuffer(output_message,outputFileName.format(i=currentCounter)) 

        #####################     Q7    #####################
        currentCounter += 1
        output_message= addDivider("")
        output_message=addInputTitle("Q7", output_message)
        
        try:
            arr = bookDB.functionQ7(3.0)

            # Header Line
            output_message=addLine("publisher_id\tpublisher_name",output_message)

            if arr is not None:
                for res in arr:
                    output_message=addLine(res,output_message)

        except Exception as e:
            output_message=addLine("Q7: Exception occurred:\n\n" + str(e),output_message)      

        output_message = addDivider(output_message)
        output_message = writeBuffer(output_message,outputFileName.format(i=currentCounter)) 

        #####################     Q8    #####################
        currentCounter += 1
        output_message= addDivider("")
        output_message=addInputTitle("Q8", output_message)
        
        try:
            arr = bookDB.functionQ8()

            # Header Line
            output_message=addLine("isbn\tbook_name\trating",output_message)

            if arr is not None:
                for res in arr:
                    output_message=addLine(res,output_message)

        except Exception as e:
            output_message=addLine("Q8: Exception occurred:\n\n" + str(e),output_message)       

        output_message = addDivider(output_message)
        output_message = writeBuffer(output_message,outputFileName.format(i=currentCounter)) 


        #####################     Q9    #####################
        currentCounter += 1
        output_message= addDivider("")
        output_message=addInputTitle("Q9", output_message)
        
        try:
            sumRating = bookDB.functionQ9("is")

            # Header Line
            output_message=addLine(f"Sum of all ratings is:{sumRating}",output_message )

        except Exception as e:
            output_message=addLine("Q9: Exception occurred:\n\n" + str(e),output_message)       

        output_message = addDivider(output_message)
        output_message = writeBuffer(output_message,outputFileName.format(i=currentCounter)) 

        #####################     Q10    #####################
        currentCounter += 1
        output_message= addDivider("")
        output_message=addInputTitle("Q10", output_message)
        
        try:
            rowCount = bookDB.function10()

            # Header Line
            output_message=addLine(f"There are {rowCount} rows in publisher table",output_message)

        except Exception as e:
            output_message=addLine("10: Exception occurred:\n\n" + str(e),output_message)       

        output_message = addDivider(output_message)
        output_message = writeBuffer(output_message,outputFileName.format(i=currentCounter)) 


    except Exception as e:
        print(e)
    finally:
        bookDB.disconnect()

if __name__ == "__main__":
    main()
