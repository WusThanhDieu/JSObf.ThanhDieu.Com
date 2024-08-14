const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const JsConfuser = require('js-confuser');
const app = express();
const port = process.env.PORT || 3000;

app.use(express.static('public'));
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());
app.use(cors());

app.post('/javascript/obfuscate', (req, res) => {
  const {
    code, target, preset, stringEncoding, stringConcealing, stringCompression,
    stringSplitting, integrity, renameVariables, renameGlobals, movedDeclarations,
    controlFlowFlattening, dispatcher, opaquePredicates, deadCode, calculator,
    domainLock, osLock, browserLock, selfDefending, antiDebug, duplicateLiteralsRemoval,
    shuffle, stack
  } = req.body;

  const startTime = Date.now();

  JsConfuser.obfuscate(code, {
    target: target,
    preset: preset,
    stringEncoding: stringEncoding,
    stringConcealing: stringConcealing,
    stringCompression: stringCompression,
    stringSplitting: stringSplitting,
    renameVariables: renameVariables,
    renameGlobals: renameGlobals,
    movedDeclarations: movedDeclarations,
    controlFlowFlattening: controlFlowFlattening,
    dispatcher: dispatcher,
    opaquePredicates: opaquePredicates,
    deadCode: deadCode,
    calculator: calculator,
    compact: true,
    hexadecimalNumbers: true,
    minify: true,
    lock: {
      integrity: integrity,
      selfDefending: selfDefending,
      antiDebug: antiDebug,
    },
    duplicateLiteralsRemoval: duplicateLiteralsRemoval,
    shuffle: shuffle,
    stack: stack,
    identifierGenerator: function () {
      return "$_THANHDIEUx待" + Math.random().toString(36).substring(7);
    },
  }).then(obfuscated => {
    const endTime = Date.now();
    const executionTime = ((endTime - startTime) / 1000).toFixed(1);
    const author = `/**
* Obf.ThanhDieu.Com Online Obfuscation Javascript :)
* Obfuscate At: ${new Date().toLocaleTimeString()} ${new Date().toLocaleDateString()}
* Preset: ${preset}
* Execution time: ${executionTime}s
*/
`;
    if (code.trim().length === 0) {
      res.send('Vui lòng dán đoạn mã cần obfuscate!');
      return;
    }
    res.send(`${author}${obfuscated}`);
  }).catch(err => {
    let error;
    if (err.message.includes('Unexpected token')) {
      error = 'Đoạn mã không đúng định dạng JavaScript.\nHoặc code của bạn có vấn đề về lỗi cú pháp.';
    } else {
      error = err.message;
    }
    res.send(error);
  });
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
