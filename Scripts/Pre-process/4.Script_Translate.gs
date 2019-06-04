function myFunction() {
  var ss = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  ss.getRange("C2").setFormula("=GOOGLETRANSLATE(B2,\"pt-br\",\"en\")");
  
  var lr = ss.getLastRow();
  var fillDownRange = ss.getRange(2, 3, lr-1);
  ss.getRange("C2").copyTo(fillDownRange);
}