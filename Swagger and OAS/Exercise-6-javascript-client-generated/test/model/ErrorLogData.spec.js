/**
 * Music API
 * **Music API with playlists**
 *
 * OpenAPI spec version: 0.3.0
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 *
 * Swagger Codegen version: 2.3.1
 *
 * Do not edit the class manually.
 *
 */

(function(root, factory) {
  if (typeof define === 'function' && define.amd) {
    // AMD.
    define(['expect.js', '../../src/index'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    factory(require('expect.js'), require('../../src/index'));
  } else {
    // Browser globals (root is window)
    factory(root.expect, root.MusicApi);
  }
}(this, function(expect, MusicApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new MusicApi.ErrorLogData();
  });

  var getProperty = function(object, getter, property) {
    // Use getter method if present; otherwise, get the property directly.
    if (typeof object[getter] === 'function')
      return object[getter]();
    else
      return object[property];
  }

  var setProperty = function(object, setter, property, value) {
    // Use setter method if present; otherwise, set the property directly.
    if (typeof object[setter] === 'function')
      object[setter](value);
    else
      object[property] = value;
  }

  describe('ErrorLogData', function() {
    it('should create an instance of ErrorLogData', function() {
      // uncomment below and update the code to test ErrorLogData
      //var instane = new MusicApi.ErrorLogData();
      //expect(instance).to.be.a(MusicApi.ErrorLogData);
    });

    it('should have the property entry (base name: "entry")', function() {
      // uncomment below and update the code to test the property entry
      //var instane = new MusicApi.ErrorLogData();
      //expect(instance).to.be();
    });

    it('should have the property _date (base name: "date")', function() {
      // uncomment below and update the code to test the property _date
      //var instane = new MusicApi.ErrorLogData();
      //expect(instance).to.be();
    });

  });

}));
