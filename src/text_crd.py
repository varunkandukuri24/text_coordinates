import sys
import fitz  # PyMuPDF
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt

class PDFViewer(QMainWindow):
    def __init__(self, pdf_path):
        super().__init__()
        self.pdf_document = fitz.open(pdf_path)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('PDF Viewer')
        self.setGeometry(100, 100, 800, 600)

        # Create a QWidget and set it as the central widget
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Create a QVBoxLayout to hold the components
        layout = QVBoxLayout()
        self.central_widget.setLayout(layout)

        # Create a QLabel to hold the PDF pixmap
        self.label = QLabel(self)
        layout.addWidget(self.label)

        # Render the first page
        self.render_page(0)

    def render_page(self, page_number):
        page = self.pdf_document.load_page(page_number)
        pix = page.get_pixmap()
        img = QImage(pix.samples, pix.width, pix.height, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(img)
        self.label.setPixmap(pixmap)

    def mousePressEvent(self, event):
        x = event.x()
        y = event.y()
        # Transform the y-coordinate
        page_height = self.pdf_document[0].bound().height  # Assuming you're dealing with the first page
        transformed_y = page_height - y
        print(f"Clicked at: ({x}, {transformed_y})")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    pdf_path = './assets/b2form.pdf'  # Change this to your PDF file path
    viewer = PDFViewer(pdf_path)
    viewer.show()
    sys.exit(app.exec_())