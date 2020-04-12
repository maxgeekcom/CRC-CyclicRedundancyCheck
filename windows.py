from tkinter import Tk, Label, filedialog, Button, Text, END, CENTER
from tkinter.ttk import Combobox
from tkinter.messagebox import showwarning, showinfo
import functions


class ParentWindow(Tk):
    """ This class describes the main parameters for all inheritable classes"""
    def __init__(self):
        Tk.__init__(self)

        self.geometry("600x400+660+340")
        self.resizable(False, False)
        self.configure(background='white')


class MainTypeWindow(ParentWindow):
    """ This class is a template for main window in app. """
    def __init__(self):
        ParentWindow.__init__(self)

    def firstLabelField(self, text):
        """ Label for description of the first button. """
        firstLabelField = Label(self,
                                text=text,
                                font="Helvetica 12 bold",
                                bg="white"
                                )
        firstLabelField.place(x=173,
                              y=80,
                              width=254,
                              height=20
                              )

    def secondLabelField(self, text):
        """ Label for description of the second button. """
        secondLabel = Label(self,
                            text=text,
                            font="Helvetica 12 bold",
                            bg="white"
                            )
        secondLabel.place(x=187,
                          y=230,
                          width=226,
                          height=20
                          )

    def firstButtonField(self, command, text):
        firstButton = Button(self,
                             text=text,
                             relief="groove",
                             bg="#87cefa",
                             command=command
                             )
        firstButton.place(x=175,
                          y=120,
                          width=250,
                          height=50
                          )

    def secondButtonField(self, commnad, text):
        secondButton = Button(self, text=text,
                              relief="groove",
                              bg="#87cefa",
                              command=commnad
                              )

        secondButton.place(x=175,
                           y=270,
                           width=250,
                           height=50
                           )


class FirstTypeWindow(ParentWindow):
    """ This class is a template of functional windows. """
    def __init__(self):
        ParentWindow.__init__(self)

        self.geometry("+665+345")

    def firstTextField(self):
        """Text field for user's message"""
        firstText = Text(self, relief="solid")
        firstText.place(x=70,
                        y=30,
                        width=460,
                        height=200
                        )
        return firstText

    def secondTextField(self):
        """Text field for path to user's file"""
        secondText = Text(self, relief="solid")
        secondText.place(x=70,
                         y=270,
                         width=360,
                         height=20
                         )
        return secondText

    def thirdTextField(self):
        """Text field for the checksum"""
        thirdText = Text(self, relief="solid")
        thirdText.place(x=70,
                        y=310,
                        width=360,
                        height=20
                        )
        return thirdText

    def firstLabelField(self, text):
        """ Description of the first field. For message text.
            Default text = "Fill message field"
        """
        firstLabel = Label(self,
                           text=text,
                           bg="white",
                           )
        firstLabel.place(x=70,
                         y=10,
                         width=68,
                         height=20
                         )

    def secondLabelField(self, text):
        """ Description of the second field. For file path.
            Default text = "Or choose a file file from your Desktop"
        """
        secondLabel = Label(self,
                            text=text,
                            bg="white",
                            )
        secondLabel.place(x=70,
                          y=250,
                          width=188,
                          height=20
                          )

    def thirdLabelField(self, text):
        """ Description of the third field. For public/private key.
            Default text = "Checksum"
        """
        thirdLabel = Label(self,
                           text=text,
                           bg="white",
                           )
        thirdLabel.place(x=70,
                         y=290,
                         width=60,
                         height=20
                         )

    def firstButtonField(self, command, text):
        """ Button for get path of file from your Desktop
            Default text = "Choose"
        """
        firstButton = Button(self,
                             text=text,
                             command=command,
                             relief="groove",
                             bg="#87cefa"
                             )
        firstButton.place(x=440,
                          y=270,
                          width=90,
                          height=20)

    def secondButtonField(self, command, text):
        """ Button for signing some item or document.
            Default text = "Sign"
        """
        secondButton = Button(self,
                              text=text,
                              relief="groove",
                              bg="#87cefa",
                              command=command
                              )
        secondButton.place(x=225,
                           y=350,
                           width=150,
                           height=30)

    def firstComboboxField(self, values):
        """ List of available CRC """
        firstCombobox = Combobox(self,
                                 values=values,
                                 justify=CENTER
                                 )

        firstCombobox.current(0)
        firstCombobox.place(x=440,
                            y=310,
                            width=90,
                            height=20
                            )
        return firstCombobox


class MainAppWindow(MainTypeWindow):
    def __init__(self):
        MainTypeWindow.__init__(self)

        self.title("CRC - Cyclic Redundancy Check")

        self.firstLabelField("Calculate checksum of text or file")
        self.firstButtonField(self.openCalculateWindow, "Calculate")

        self.secondLabelField("Verify checksum of text or file")
        self.secondButtonField(self.openCheckWindow, "Check")

    def openCalculateWindow(self):
        CalculateWindow()

    def openCheckWindow(self):
        VerifykWindow()


class CalculateWindow(FirstTypeWindow):
    """ Class, which describes window, where you can calculate checksum. """
    def __init__(self):
        FirstTypeWindow.__init__(self)

        self.title("Calculate checksum")

        self.firstLabelField("Fill text field")
        self.mesText = self.firstTextField()

        self.secondLabelField("Or choose a file from your Desktop")
        self.pathFileText = self.secondTextField()
        self.firstButtonField(self.choosePathToFile, "Choose")

        self.thirdLabelField("Checksum")
        self.checkSumText = self.thirdTextField()

        self.listCRC = self.firstComboboxField(list(functions.polynomials.keys()))

        self.secondButtonField(self.calculateChecksum, "Calculate")

    def choosePathToFile(self):

        filename = filedialog.askopenfilename(parent=self)
        self.pathFileText.delete(1.0, END)
        self.pathFileText.insert(1.0, filename)

    def calculateChecksum(self):

        valueMesText = self.mesText.get(1.0, END).rstrip()
        valuePathFileText = self.pathFileText.get(1.0, END).rstrip()

        if valueMesText == '' and valuePathFileText == '':
            showwarning("Warning!", "Please, fill message field or path of file field!", parent=self)

        elif self.mesText.get(1.0, END).rstrip() != '' and self.pathFileText.get(1.0, END).rstrip() != '':
            showwarning("Warning!", "You can fill only one field. Message or path to file!", parent=self)

        elif valueMesText != '' and valuePathFileText == '':
            textInt = functions.getPosSumText(self.mesText.get(1.0, END).rstrip())
            polynomial = functions.polynomials[self.listCRC.get()]

            checkSum = functions.calculateCheckSum(textInt, polynomial)
            checkSumHex = hex(checkSum)[2:]

            self.checkSumText.delete(1.0, END)
            self.checkSumText.insert(1.0, checkSumHex)

            showinfo("Info", "Checksum was calculated!", parent=self)

        elif valueMesText == '' and valuePathFileText != '':

            pathAndFilename = self.pathFileText.get(1.0, END).rstrip()
            fileInt = functions.getPosSumFile(pathAndFilename)

            polynomial = functions.polynomials[self.listCRC.get()]

            checkSum = functions.calculateCheckSum(fileInt, polynomial)
            checkSumHex = hex(checkSum)[2:]

            self.checkSumText.delete(1.0, END)
            self.checkSumText.insert(1.0, checkSumHex)

            showinfo("Info", "Checksum was calculated!", parent=self)


class VerifykWindow(FirstTypeWindow):
    """ Class, which describes window, where you can verify checksum. """
    def __init__(self):
        FirstTypeWindow.__init__(self)

        self.title("Verify checksum")

        self.firstLabelField("Fill text field")
        self.mesText = self.firstTextField()

        self.secondLabelField("Or choose a file from your Desktop")
        self.pathFileText = self.secondTextField()
        self.firstButtonField(self.choosePathToFile, "Choose")

        self.thirdLabelField("Checksum")
        self.checkSumText = self.thirdTextField()

        self.listCRC = self.firstComboboxField(list(functions.polynomials.keys()))

        self.secondButtonField(self.verifyCheckSum, "Verify")

    def verifyCheckSum(self):

        valueMesText = self.mesText.get(1.0, END).rstrip()
        valuePathFileText = self.pathFileText.get(1.0, END).rstrip()
        valueCheckSumText = self.checkSumText.get(1.0, END).rstrip()

        if valueMesText == '' and valuePathFileText == '':
            showwarning("Warning!", "Please, fill message field or path of file field!", parent=self)

        elif valueMesText != '' and valuePathFileText != '':
            showwarning("Warning!", "You can fill only one field. Message or path to file!", parent=self)

        elif valueCheckSumText == '':
            showwarning("Warning!", "Please, fill checksum field!", parent=self)

        elif valueMesText != '' and valuePathFileText == '':
            textInt = functions.getPosSumText(self.mesText.get(1.0, END).rstrip())
            polynomial = functions.polynomials[self.listCRC.get()]
            checkSum = int(self.checkSumText.get(1.0, END).rstrip(), 16)

            if functions.verifyCheckSum(textInt, checkSum, polynomial):
                showinfo("Info", "Text integrity is not broken.", parent=self)
            else:
                showinfo("Info", "Text integrity is broken.", parent=self)

        elif valueMesText == '' and valuePathFileText != '':

            pathAndFilename = self.pathFileText.get(1.0, END).rstrip()
            fileInt = functions.getPosSumFile(pathAndFilename)
            checkSum = int(self.checkSumText.get(1.0, END).rstrip(), 16)
            polynomial = functions.polynomials[self.listCRC.get()]

            if functions.verifyCheckSum(fileInt, checkSum, polynomial):
                showinfo("Info", "File integrity is not broken.", parent=self)
            else:
                showinfo("Info", "File integrity is broken.", parent=self)

    def choosePathToFile(self):
        CalculateWindow.choosePathToFile(self)
