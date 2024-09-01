# Công cụ mã hoá JavaScript ngăn chặn các king of copy không thể chỉnh sửa được. [trang mã hoá online](https://fakebill.thanhdieutv.com/tools/obfuscate-javascript).

### Cách sử dụng:

Ở đây tôi sử dụng thư viện mã hoá có sẵn của JsConfuser, để thực thi trên môi trường nodejs.

```javascript
var JsConfuser = require("js-confuser");
JsConfuser.obfuscate(`
 function HelloWorld() {
 alert("Obf.ThanhDieu.Com");
 }
 HelloWorld();
`, {
  target: "browser",
  preset: "low",
  stringEncoding: true,
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
| target | string |
| preset | string |
| stringEncoding | boolean |
| stringConcealing | boolean |
| stringCompression | boolean |
| stringSplitting | boolean |
| integrity | boolean |
| renameVariables | boolean |
| renameGlobals | boolean |
| movedDeclarations | boolean |
| controlFlowFlattening | boolean |
| dispatcher | boolean |
| opaquePredicates | boolean |
| deadCode | boolean |
| calculator | boolean |
| domainLock | array |
| osLock | array |
| browserLock | array |
| selfDefending | boolean |
| antiDebug | boolean |
| duplicateLiteralsRemoval | boolean |
| shuffle | boolean |
| stack | boolean |

### Ảnh demo:

![ThanhDieu.Com](https://i.imgur.com/IIaj1gM.png)
