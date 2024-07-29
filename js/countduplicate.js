var itemName = ["box","gloves","shirts","shirts","gloves"]
var price = [2,1,3,2,1]
var weight = [3,1,4,4,1]

function CountDuplicates(itemName, price, weight){
    let duplicates=0;
    let itemsDict = {}
    for(var i=0; i<itemName.length;i++){       
        const key = `${itemName[i]}-${price[i]}-${weight[i]}}`;
        console.log(`Key is - ${key}`);
        if(itemsDict.hasOwnProperty(key)){
            itemsDict[key]+=1;
            duplicates+=1;
        }
        else{
            itemsDict[key] = 1;
        }
    }
    return duplicates
}

console.log(`Duplicates are - ${CountDuplicates(itemName, price, weight)}`)