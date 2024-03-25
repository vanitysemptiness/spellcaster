import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QWidget, QTreeWidget, QTreeWidgetItem, QLabel, QGraphicsView, QGraphicsScene, QGraphicsTextItem
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QTextCursor
from PyPDF2 import PdfReader
import fitz

class PDFInspector(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Create main widget and layout
        central_widget = QWidget(self)
        layout = QHBoxLayout(central_widget)
        self.setCentralWidget(central_widget)

        # Create tree view for PDF object tree
        self.tree_widget = QTreeWidget()
        self.tree_widget.setHeaderLabels(['Object', 'Value'])
        layout.addWidget(self.tree_widget)

        # Create PDF renderer widget
        self.pdf_view = QGraphicsView()
        self.pdf_scene = QGraphicsScene()
        self.pdf_view.setScene(self.pdf_scene)
        layout.addWidget(self.pdf_view)

    def drag_enter_event(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def drop_event(self, event):
        if event.mimeData().hasUrls():
            file_path = event.mimeData().urls()[0].toLocalFile()
            self.load_pdf(file_path)

    def load_pdf(self, file_path):
        try:
            with open(file_path, 'rb') as file:
                reader = PdfReader(file)
                self.populate_tree(reader)
                self.render_pdf(file_path)
        except Exception as e:
            print(f"Error loading PDF: {e}")

    def populate_tree(self, reader):
        # Clear existing tree items
        self.tree_widget.clear()

        # Traverse PDF object tree and populate tree view
        try:
            for page in reader.pages:
                self.add_tree_items(page)
        except Exception as e:
            print(f"Error populating tree: {e}")

    def add_tree_items(self, obj, parent=None):
        if isinstance(obj, dict):
            for key, value in obj.items():
                if isinstance(value, (dict, list)):
                    item = QTreeWidgetItem([key, ''])
                    if parent:
                        parent.addChild(item)
                    else:
                        self.tree_widget.addTopLevelItem(item)
                    self.add_tree_items(value, item)
                else:
                    item = QTreeWidgetItem([key, str(value)])
                    if parent:
                        parent.addChild(item)
                    else:
                        self.tree_widget.addTopLevelItem(item)
        elif isinstance(obj, list):
            for i, value in enumerate(obj):
                if isinstance(value, (dict, list)):
                    item = QTreeWidgetItem([str(i), ''])
                    if parent:
                        parent.addChild(item)
                    else:
                        self.tree_widget.addTopLevelItem(item)
                    self.add_tree_items(value, item)
                else:
                    item = QTreeWidgetItem([str(i), str(value)])
                    if parent:
                        parent.addChild(item)
                    else:
                        self.tree_widget.addTopLevelItem(item)

    def render_pdf(self, file_path):
        # Clear existing PDF scene
        self.pdf_scene.clear()

        # Open PDF document
        doc = fitz.open(file_path)

        # Render each page of the PDF
        for page_num in range(doc.page_count):
            page = doc.load_page(page_num)
            pix = page.get_pixmap()
            img = pix.tobytes()

            # Create QImage from the pixel data
            qimg = QImage(img, pix.width, pix.height, QImage.Format_RGB888)

            # Create QGraphicsPixmapItem from the QImage
            pixmap_item = QGraphicsPixmapItem(QPixmap.fromImage(qimg))

            # Add the pixmap item to the scene
            self.pdf_scene.addItem(pixmap_item)

            # Set the position of the pixmap item
            pixmap_item.setPos(0, page_num * pix.height)

            # Extract text from the page
            text = page.get_text("text")

            # Create QGraphicsTextItem for the page text
            text_item = QGraphicsTextItem(text)
            text_item.setDefaultTextColor(QColor("transparent"))

            # Set the position of the text item
            text_item.setPos(0, page_num * pix.height)

            # Add the text item to the scene
            self.pdf_scene.addItem(text_item)

            # Connect the text selection signal to the highlight function
            text_item.document().contentsChanged.connect(lambda item=text_item: self.highlight_text(item))

        # Set the scene rect to fit the rendered pages
        self.pdf_scene.setSceneRect(self.pdf_scene.itemsBoundingRect())

    def highlight_text(self, text_item):
        # Get the selected text cursor
        cursor = text_item.textCursor()

        # Check if there is a selection
        if cursor.hasSelection():
            # Get the selected text
            selected_text = cursor.selectedText()

            # Find the corresponding tree item for the selected text
            tree_item = self.find_tree_item(selected_text)

            if tree_item:
                # Highlight the corresponding tree item
                self.tree_widget.setCurrentItem(tree_item)
                tree_item.setBackground(0, QColor("yellow"))
                tree_item.setBackground(1, QColor("yellow"))
        else:
            # Remove the highlight from the tree item
            self.remove_tree_highlight()

    def find_tree_item(self, text):
        # Recursively search for the tree item containing the given text
        def search_tree(item):
            if item.text(1) == text:
                return item
            for i in range(item.childCount()):
                result = search_tree(item.child(i))
                if result:
                    return result
            return None

        # Search from the root item of the tree
        root_item = self.tree_widget.invisibleRootItem()
        return search_tree(root_item)

    def remove_tree_highlight(self):
        # Remove the highlight from all tree items
        def remove_highlight(item):
            item.setBackground(0, QColor("white"))
            item.setBackground(1, QColor("white"))
            for i in range(item.childCount()):
                remove_highlight(item.child(i))

        # Start from the root item of the tree
        root_item = self.tree_widget.invisibleRootItem()
        remove_highlight(root_item)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    inspector = PDFInspector()
    inspector.show()
    sys.exit(app.exec_())