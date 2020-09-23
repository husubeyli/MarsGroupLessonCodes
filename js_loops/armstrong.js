for (var i = 1; i < 10; i++ ){
    for(var j=0; i < 10; j++ ){
        for(var k=0; k < 10; k++ ){
            var a = i * 100 + j * 10 + k * 1;
            // console.log(a);
            var b = Math.pow(i, 3) + Math.pow(j, 3) + Math.pow(k, 3);
            if (a === b){
                console.log((i*100 + j*10 + k*1 +  ' is Armstrong number'));
                // break;
            }
        }
    }
}

// for (var i = 1; i < 10; i++ ){
//     for (var j = 1; j < 10; j++){
//         for(var k = 1; k < 10; k++){
//             if (Math.pow(i,3) + Math.pow(j,3) + Math.pow(k,3) === (i * 100 + j * 10 + k*1)){
//             console.log((i * 100 + j * 10 + k*1 + ' is Armstrong number'));
//             }
//         }
//     }
// }
