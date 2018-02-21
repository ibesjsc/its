/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package MainProg;

import com.sun.org.apache.xalan.internal.xsltc.compiler.util.CompareGenerator;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.DirectoryIteratorException;
import java.nio.file.DirectoryStream;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

/**
 *
 * @author Luzec 
 */
public class MainProg {

    /**
     * @param args the command line arguments
     */
    
    public static void PreprocessingCase2(String dirName) throws IOException{ 
        File dir = new File(dirName);       
        // list the files using our FileFilter
        File[] files = dir.listFiles();
        for (File f : files)
        {
            String fileName = f.getName();
            System.out.println("file: " + f.getAbsolutePath());
            Case2.ProcessingDataTimeStep_1_Feature_k("E:\\PhD-Research\\Data_Experiment\\Non_Cutting_Data\\DataByDate\\"+fileName,"E:\\PhD-Research\\Data_Experiment\\Non_Cutting_Data\\ResultCutting\\"+fileName+"-OUT");
        }
    }
    
    public static void main(String[] args) throws IOException {
        // TODO code application logic here
        //Case1.ProcessingDataTimeStep_1_Feature_1("E:\\PhD-Research\\Data_Experiment\\Non_Cutting_Data\\_75.csv","E:\\PhD-Research\\Data_Experiment\\Non_Cutting_Data\\OUT_RAW_CASE1.csv");
        //Case2.ProcessingDataTimeStep_1_Feature_k("E:\\PhD-Research\\Data_Experiment\\Non_Cutting_Data\\_75.csv","E:\\PhD-Research\\Data_Experiment\\Non_Cutting_Data\\OUT_RAW_CASE2.csv");
        //Case3.ProcessingDataTimeStep_k_Feature_2("E:\\PhD-Research\\Data_Experiment\\Non_Cutting_Data\\_75.csv","E:\\PhD-Research\\Data_Experiment\\Non_Cutting_Data\\OUT_RAW_CASE3.csv");
        //Case4.ProcessingDataTimeStep_k_Feature_3("E:\\PhD-Research\\Data_Experiment\\Non_Cutting_Data\\_75.csv","E:\\PhD-Research\\Data_Experiment\\Non_Cutting_Data\\OUT_RAW_CASE4.csv");
        
        //CuttingDataByDay.DataByDay("E:\\\\PhD-Research\\\\Data_Experiment\\\\Non_Cutting_Data\\\\20_80.csv");
        
        //PreprocessingCase2("E:\\PhD-Research\\Data_Experiment\\Non_Cutting_Data\\DataByDate");
    }
    
}
