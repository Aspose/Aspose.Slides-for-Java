/* 
 * Copyright 2001-2013 Aspose Pty Ltd. All Rights Reserved.
 *
 * This file is part of Aspose.Slides. The source code in this file
 * is only intended as a supplement to the documentation, and is provided
 * "as is", without warranty of any kind, either expressed or implied.
 */
 
package com.aspose.slides.examples.Presentation.ManageProperties;

import com.aspose.slides.*;
import com.aspose.slides.examples.Utils;

public class AccessBuiltinProperties
{
    public static void main(String[] args) throws Exception
    {
        // The path to the documents directory.
        String dataDir = Utils.getDataDir(AccessBuiltinProperties.class);

        //Instantiate the Presentation class that represents the Presentation1
        Presentation pres = new Presentation(dataDir+ "Aspose.pptx");

        //Create a reference to IDocumentProperties object associated with Presentation
        IDocumentProperties dp = pres.getDocumentProperties();

        //Display the builtin properties
        System.out.println("Category : " + dp.getCategory());
        System.out.println("Current Status : " + dp.getContentStatus());
        System.out.println("Creation Date : " + dp.getCreatedTime());
        System.out.println("Author : " + dp.getAuthor());
        System.out.println("Description : " + dp.getComments());
        System.out.println("KeyWords : " + dp.getKeywords());
        System.out.println("Last Modified By : " + dp.getLastSavedBy());
        System.out.println("Supervisor : " + dp.getManager());
        System.out.println("Modified Date : " + dp.getLastSavedTime());
        System.out.println("Presentation Format : " + dp.getPresentationFormat());
        System.out.println("Last Print Date : " + dp.getLastPrinted());
        System.out.println("Is Shared between producers : " + dp.getSharedDoc());
        System.out.println("Subject : " + dp.getSubject());
        System.out.println("Title : " + dp.getTitle());

        System.out.println("Program executed successfully");
    }
}




