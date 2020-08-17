import __main__,slicer,qt
from DICOMLib import DICOMUtils
customLayout = """
<layout type="vertical" split="true">
  <item>
   <view class="vtkMRMLViewNode" singletontag="1">
     <property name="viewlabel" action="default">1</property>
   </view>
  </item>
</layout>
"""
customLayoutId = 3
mainWidget = qt.QWidget()
mainWidget.objectName = "qSlicerAppMainWindow"
vlayout = qt.QVBoxLayout()
mainWidget.setLayout(vlayout)
layoutWidget = slicer.qMRMLLayoutWidget()
layoutManager = slicer.qSlicerLayoutManager()
layoutManager.setMRMLScene(slicer.mrmlScene)
layoutManager.setScriptedDisplayableManagerDirectory(slicer.app.slicerHome + "/bin/Python/mrmlDisplayableManager")
layoutWidget.setLayoutManager(layoutManager)
layoutManager.layoutLogic().GetLayoutNode().AddLayoutDescription(customLayoutId, customLayout)
layoutManager.setLayout(customLayoutId)
vlayout.addWidget(layoutWidget)
dicomDataDir = "/home/xand/Downloads/dicom/some/"  # input folder with DICOM files
loadedNodeIDs = []
with DICOMUtils.TemporaryDICOMDatabase() as db:
  DICOMUtils.importDicom(dicomDataDir, db)
  patientUIDs = db.patients()
  for patientUID in patientUIDs:
    loadedNodeIDs.extend(DICOMUtils.loadPatientByUID(patientUID))
mainWidget.show()
__main__.mainWidget = mainWidget
