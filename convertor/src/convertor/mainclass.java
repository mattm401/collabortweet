package convertor;

import java.util.ArrayList;
import java.util.Arrays;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Iterator;
import java.util.List;
import java.util.StringTokenizer;

import com.univocity.parsers.csv.CsvParser;
import com.univocity.parsers.csv.CsvParserSettings;

import java.io.StringReader;


public class mainclass {

	public static void main(String[] args) throws FileNotFoundException{
	   
	    
	    
	    CsvParserSettings settings = new CsvParserSettings();
	    //the file used in the example uses '\n' as the line separator sequence.
	    //the line separator sequence is defined here to ensure systems such as MacOS and Windows
	    //are able to process this file correctly (MacOS uses '\r'; and Windows uses '\r\n').
	    settings.getFormat().setLineSeparator("\n");
	    
	    
	    CsvParser parser = new CsvParser(settings);

	    // call beginParsing to read records one by one, iterator-style.
	    parser.beginParsing(new FileReader("./input.csv"));

	    String[] row;
	    List<List<String>> stats = new ArrayList<List<String>>();
	    
	    //x.add("Hello");
	    //x.add("world!");
	  //  stats.add(x);
	    boolean isSecondRow = false;
	    int elementCount = 1;
	    
	   // System.out.println(Arrays.deepToString(stats.toArray()));
	    List<String[]> originial = new ArrayList<String[]>();
	    while ((row = parser.parseNext()) != null) {
	    	
	    	//System.out.println(Arrays.toString(row));
	    	originial.add(row);
	    	
	    }
	    List<String> first = new ArrayList<String>();
	   // System.out.println(originial);
	    
	    first.add("elementId");
	    first.add("Product Review (2)");
	    first.add("Product Review (7)");
	    first.add("News Coverage (2)");
	    first.add("News Coverage (7)");
	    first.add("Unboxing (2)");
	    first.add("Unboxing (7)");
	    first.add("Demonstration (2)");
	    first.add("Demonstration (7)");
	    first.add("Advertisement (2)");
	    first.add("Advertisement (7)");
	    first.add("Unstructured Use (2)");
	    first.add("Unstructured Use (7)");
	    first.add("Unsure (2)");
	    first.add("Unsure (7)");
	    first.add("Not Relevent (2)");
	    first.add("Not Relevent (7)");
	    first.add("id");
	    
	    stats.add(first);
	    for (int i = 0; i < originial.size()-1; i++) {
	    	List<String> x = new ArrayList<String>();
	    	
	       	if (!isSecondRow) {
	    		x.add(Integer.toString(elementCount));
	    		x.add("0");
	    		
	    		x.add(2, "0");
	    		x.add(3, "0");
	    		x.add(4, "0");
	    		x.add(5, "0");
	    		x.add(6, "0");
	    		x.add(7, "0");
	    		x.add(8, "0");
	    		x.add(9, "0");
	    		x.add(10, "0");
	    		x.add(11, "0");
	    		x.add(12, "0");
	    		x.add(13, "0");
	    		x.add(14, "0");
	    		x.add(15, "0");
	    		x.add(16, "0");
	    		x.add(17, originial.get(i)[0]);

	    		if (originial.get(i)[2].equals("1")) {
	    			//System.out.println(originial.get(i)[2] );
	    			x.set(1, "1");
	    		} else if (originial.get(i)[2].equals("2")) {
	    			//System.out.println(i[2] );
	    			x.set(3, "1");
	    		} else if (originial.get(i)[2].equals("3")) {
	    			//System.out.println(i[2] );
	    			x.set(5, "1");
	    		} else if (originial.get(i)[2].equals("4")) {
	    			//System.out.println(i[2] );
	    			x.set(7, "1");
	    		} else if (originial.get(i)[2].equals("5")) {
	    			//System.out.println(i[2] );
	    			x.set(9, "1");
	    		} else if (originial.get(i)[2].equals("6")) {
	    			//System.out.println(i[2] );
	    			x.set(11, "1");
	    		} else if (originial.get(i)[2].equals("7")) {
	    			//System.out.println(i[2] );
	    			x.set(13, "1");
	    		} else if (originial.get(i)[2].equals("8")) {
	    			//System.out.println(i[2] );
	    			x.set(15, "1");
	    		}
	    		
	       		if (originial.get(i+1)[2].equals("1")) {
	    			x.set(2, "1");
	    		} else if (originial.get(i+1)[2].equals("2")) {
	    			x.set(4, "1");
	    		} else if (originial.get(i+1)[2].equals("3")) {
	    			x.set(6, "1");
	    		} else if (originial.get(i+1)[2].equals("4")) {
	    			x.set(8, "1");
	    		} else if (originial.get(i+1)[2].equals("5")) {
	    			x.set(10, "1");
	    		} else if (originial.get(i+1)[2].equals("6")) {
	    			x.set(12, "1");
	    		} else if (originial.get(i+1)[2].equals("7")) {
	    			x.set(14, "1");
	    		} else if (originial.get(i+1)[2].equals("8")) {
	    			x.set(16, "1");
	    		}
	    		// System.out.println(Arrays.toString(row));
	    		 //System.out.println("hey" + x);
	    		elementCount++;
	    		//System.out.println(x);
	    		isSecondRow = true;
	    		stats.add(x);
	    	//	System.out.println(x);
	    		
	    	} else {
	    		isSecondRow = false;
	    	}
	    	
	    	
	    }
	    
	    
	    
	    
	   // System.out.println(Arrays.deepToString(stats.toArray()));
	    
	    
	    
	    
	    
	    
	    
	    StringBuilder builder = new StringBuilder();
	    for(int i = 0; i < stats.size(); i++)//for each row
	    	
	    {
	    	
	       for(int j = 0; j < stats.get(0).size(); j++)//for each column
	       {
	    	  
	          builder.append(stats.get(i).get(j)+"");//append to the output string
	          if(j < stats.get(0).size() - 1)//if this is not the last row element
	             builder.append(",");//then add comma (if you don't like commas you can use spaces)
	       }
	       builder.append("\n");//append new line at the end of the row
	    }
	    System.out.println(builder);
	    
	    
	    try {
	    	BufferedWriter writer = new BufferedWriter (new FileWriter("./convert.txt"));
	    	
	    	writer.write(builder.toString());
	    	
	    	writer.close();
	    } catch (IOException e) {
	    	
	    }
	    /*
	    while ((row = parser.parseNext()) != null) {
	    	
	    	if ( row[0] !="externalId") {
	    		//System.out.println(row[0] );
	    	
	    	if (!isSecondRow) {
	    		x.add(Integer.toString(elementCount));
	    		x.add("0");
	    		
	    		x.add(2, "0");
	    		x.add(3, "0");
	    		x.add(4, "0");
	    		x.add(5, "0");
	    		x.add(6, "0");
	    		x.add(7, "0");
	    		x.add(8, "0");
	    		x.add(9, "0");
	    		x.add(10, "0");
	    		x.add(11, "0");
	    		x.add(12, "0");
	    		x.add(13, "0");
	    		x.add(14, "0");
	    		x.add(15, "0");
	    		x.add(16, "0");
	    		System.out.println(row[2] );
	    		if (row[2] != "0") {
	    			System.out.println(row[2] );
	    			x.set(1, "1");
	    		} else if (row[2] == "2") {
	    			System.out.println(row[2] );
	    			x.set(3, "1");
	    		} else if (row[2] == "3") {
	    			System.out.println(row[2] );
	    			x.set(5, "1");
	    		} else if (row[2] == "4") {
	    			System.out.println(row[2] );
	    			x.set(7, "1");
	    		} else if (row[2] == "5") {
	    			System.out.println(row[2] );
	    			x.set(9, "1");
	    		} else if (row[2] == "6") {
	    			System.out.println(row[2] );
	    			x.set(11, "1");
	    		} else if (row[2] == "7") {
	    			System.out.println(row[2] );
	    			x.set(13, "1");
	    		} else if (row[2] == "8") {
	    			System.out.println(row[2] );
	    			x.set(15, "1");
	    		}
	    		isSecondRow = true;
	    		
	    	} else {
	    	
	    		if (row[2] == "1") {
	    			x.set(2, "1");
	    		} else if (row[2] == "2") {
	    			x.set(4, "1");
	    		} else if (row[2] == "3") {
	    			x.set(6, "1");
	    		} else if (row[2] == "4") {
	    			x.set(8, "1");
	    		} else if (row[2] == "5") {
	    			x.set(10, "1");
	    		} else if (row[2] == "6") {
	    			x.set(12, "1");
	    		} else if (row[2] == "7") {
	    			x.set(14, "1");
	    		} else if (row[2] == "8") {
	    			x.set(16, "1");
	    		}
	    		// System.out.println(Arrays.toString(row));
	    		 System.out.println("hey" + x);
	    		isSecondRow = false;
	    		stats.add(x);
	    		x.clear();
	    	}
	    	}
	    }
	    System.out.println(Arrays.deepToString(stats.toArray()));
*/
}
	
}