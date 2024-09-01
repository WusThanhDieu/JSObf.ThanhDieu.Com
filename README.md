# Công cụ mã hoá JavaScript ngăn chặn các human copy không thể chỉnh sửa được. [trang mã hoá online](https://fakebill.thanhdieutv.com/tools/obfuscate-javascript).

### Cách sử dụng:

Ở đây tôi sử dụng thư viện mã hoá có sẵn của JsConfuser, để thực thi trên môi trường nodejs.

```javascript
var JsConfuser = require("js-confuser");
JsConfuser.obfuscate(`
  function fibonacci(num){   
    var a = 0, b = 1, c = num;
    while (num-- > 1) {
      c = a + b;
      a = b;
      b = c;
    }
    return c;
  }

  for ( var i = 1; i <= 25; i++ ) {
    console.log(i, fibonacci(i))
  }
`, {
  target: "node",
  preset: "high",
  stringEncoding: false, // <- Normally enabled
}).then(obfuscated => {
  console.log(obfuscated)
})
```
### Tham số:
+ Method: POST
+ Type: JSON

### Option:
| Parameter | Type |
| --- | --- |
| target | string (browser | nodejs) |
| preset | string (low | medium | high) |
| stringEncoding | boolean (true or false) |
| stringConcealing | boolean (true or false) |
| stringCompression | boolean (true or false) |
| stringSplitting | boolean (true or false) |
| integrity | boolean (true or false) |
| renameVariables | boolean (true or false) |
| renameGlobals | boolean (true or false) |
| movedDeclarations | boolean (true or false) |
| controlFlowFlattening | boolean (true or false) |
| dispatcher | boolean (true or false) |
| opaquePredicates | boolean (true or false) |
| deadCode | boolean (true or false) |
| calculator | boolean (true or false) |
| domainLock | array (["mywebsite.com"]) |
| osLock | array (["windows", "linux"]) |
| browserLock | array (["firefox"]) |
| selfDefending | boolean (true or false) |
| antiDebug | boolean (true or false) |
| duplicateLiteralsRemoval | boolean (true or false) |
| shuffle | boolean (true or false) |
| stack | boolean (true or false) |

### Ảnh demo:

![ThanhDieu.Com](https://i.imgur.com/IIaj1gM.png)
