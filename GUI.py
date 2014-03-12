def GUI_start():
  import javax.swing as swing
  window = swing.JFrame("Test",size=(300,300))
  text_field=swing.JTextField(preferredSize=(300, 20))
  text_field.text = "Welcome to test sample!"
  window.contentPane.add(text_field)
  window.visible=1
  button = swing.JButton("View", preferredSize=(300, 20))
  window.contentPane.add(button)
  window.visible=1
  window.pack()
  window.visible=1
  
def GUI_advanced():
  