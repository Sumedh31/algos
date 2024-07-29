function printPyramid(rows){
    let spaces = rows +3;
    for(var i=0; i<rows;i++){
        for(var j=0;j<spaces - i;j++){
            process.stdout.write(' ');
        }
        for(var k =0; k<i;k++){
            process.stdout.write('P ');
        }
        process.stdout.write('\n');
    }
}

printPyramid(5);