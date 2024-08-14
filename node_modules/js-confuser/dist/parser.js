"use strict";

Object.defineProperty(exports, "__esModule", {
  value: true
});
exports.default = parseJS;
exports.parseSnippet = parseSnippet;
exports.parseSync = parseSync;
var assert = _interopRequireWildcard(require("assert"));
function _getRequireWildcardCache(e) { if ("function" != typeof WeakMap) return null; var r = new WeakMap(), t = new WeakMap(); return (_getRequireWildcardCache = function (e) { return e ? t : r; })(e); }
function _interopRequireWildcard(e, r) { if (!r && e && e.__esModule) return e; if (null === e || "object" != typeof e && "function" != typeof e) return { default: e }; var t = _getRequireWildcardCache(r); if (t && t.has(e)) return t.get(e); var n = { __proto__: null }, a = Object.defineProperty && Object.getOwnPropertyDescriptor; for (var u in e) if ("default" !== u && {}.hasOwnProperty.call(e, u)) { var i = a ? Object.getOwnPropertyDescriptor(e, u) : null; i && (i.get || i.set) ? Object.defineProperty(n, u, i) : n[u] = e[u]; } return n.default = e, t && t.set(e, n), n; }
const acorn = require("acorn");

/**
 * Uses `acorn` to parse Javascript Code. Returns an AST tree.
 * @param code
 * @returns
 */
async function parseJS(code) {
  assert.ok(typeof code === "string", "code must be a string");
  try {
    var parsed = parseSync(code);
    return parsed;
  } catch (e) {
    throw e;
  }
}

/**
 * Parses a snippet code. Returns an AST Tree.
 * @param code
 * @returns
 */
function parseSnippet(code) {
  return acorn.parse(code, {
    ecmaVersion: "latest",
    allowReturnOutsideFunction: true,
    sourceType: "module"
  });
}

/**
 * Parses synchronously. Attempts to parse as a es-module, then fallbacks to a script.
 * @param code
 * @returns
 */
function parseSync(code) {
  try {
    return acorn.parse(code, {
      ecmaVersion: "latest",
      sourceType: "module"
    });
  } catch (e) {
    return acorn.parse(code, {
      ecmaVersion: "latest",
      sourceType: "script"
    });
  }
}