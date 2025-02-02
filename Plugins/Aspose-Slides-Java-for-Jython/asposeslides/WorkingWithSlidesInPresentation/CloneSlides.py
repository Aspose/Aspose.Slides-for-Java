from asposeslides import Settings
from com.aspose.slides import Presentation
from com.aspose.slides import SaveFormat

class ChangingPosition:

    def __init__(self):
              
        # Within the Same Presentation from One Position to the End
        self.clone_to_end_of_presentation()

        # From One Position to Anther within the Same Presentation
        self.clone_to_aonther_position()

        # In Another Presentation at the End of the Existing Slides
        self.clone_to_other_presentation_at_end_of_existing_slide()
        
    def clone_to_end_of_presentation(dataDir):
        
        dataDir = Settings.dataDir + 'WorkingWithSlidesInPresentation/ChangingPosition/'    
        
        # Instantiate Presentation class that represents the presentation file

        pres = Presentation(dataDir + 'Aspose.pptx')

        # Clone the desired slide to the end of the collection of slides in the same presentation
        slides = pres.getSlides()
        slides.addClone(pres.getSlides().get_Item(0))

        # Saving the presentation file
        save_format = SaveFormat
        pres.save(dataDir + "Aspose_Cloned.pptx", save_format.Pptx)

        print "Slide has been cloned, please check the output file."
        
    def clone_to_aonther_position(dataDir):
        dataDir = Settings.dataDir + 'WorkingWithSlidesInPresentation/ChangingPosition/'
        
        # Instantiate Presentation class that represents the presentation file
        pres = Presentation(dataDir + 'Aspose.pptx')

        # Clone the desired slide to the end of the collection of slides in the same presentation
        slides = pres.getSlides()

        # Clone the desired slide to the specified index in the same presentation
        slides.insertClone(2, pres.getSlides().get_Item(1))

        # Saving the presentation file
        save_format = SaveFormat
        pres.save(dataDir + "Aspose_Cloned.pptx", save_format.Pptx)

        print "Slide has been cloned, please check the output file."
        
    def clone_to_other_presentation_at_end_of_existing_slide(dataDir):
        dataDir = Settings.dataDir + 'WorkingWithSlidesInPresentation/ChangingPosition/'        
        
        # Instantiate Presentation class that represents the presentation file
        src_pres = Presentation(dataDir + 'Aspose.pptx')

        # Instantiate Presentation class for destination PPTX (where slide is to be cloned)
        dest_pres = Presentation()

        # Clone the desired slide from the source presentation to the end of the collection of slides in destination presentation
        slds = dest_pres.getSlides()

        slds.addClone(src_pres.getSlides().get_Item(0))

        # Saving the presentation file
        save_format = SaveFormat
        dest_pres.save(dataDir + "Aspose_dest2.pptx", save_format.Pptx)

        print "Slide has been cloned, please check the output file."



if __name__ == '__main__':        
    ChangingPosition()