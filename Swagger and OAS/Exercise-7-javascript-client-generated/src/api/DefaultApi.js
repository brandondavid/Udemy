/**
 * Meme Meister
 * API to create memes
 *
 * OpenAPI spec version: 0.1.0
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
    // AMD. Register as an anonymous module.
    define(['ApiClient', 'model/MemeInfo'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    module.exports = factory(require('../ApiClient'), require('../model/MemeInfo'));
  } else {
    // Browser globals (root is window)
    if (!root.MemeMeister) {
      root.MemeMeister = {};
    }
    root.MemeMeister.DefaultApi = factory(root.MemeMeister.ApiClient, root.MemeMeister.MemeInfo);
  }
}(this, function(ApiClient, MemeInfo) {
  'use strict';

  /**
   * Default service.
   * @module api/DefaultApi
   * @version 0.1.0
   */

  /**
   * Constructs a new DefaultApi. 
   * @alias module:api/DefaultApi
   * @class
   * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
   * default to {@link module:ApiClient#instance} if unspecified.
   */
  var exports = function(apiClient) {
    this.apiClient = apiClient || ApiClient.instance;


    /**
     * Callback function to receive the result of the memeGet operation.
     * @callback module:api/DefaultApi~memeGetCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/MemeInfo>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get meme(s)
     * Returns one or more memes
     * @param {Object} opts Optional parameters
     * @param {String} opts.q Optional URL-encoded search term
     * @param {module:api/DefaultApi~memeGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/MemeInfo>}
     */
    this.memeGet = function(opts, callback) {
      opts = opts || {};
      var postBody = null;


      var pathParams = {
      };
      var queryParams = {
        'q': opts['q'],
      };
      var collectionQueryParams = {
      };
      var headerParams = {
      };
      var formParams = {
      };

      var authNames = ['oauthFacebook'];
      var contentTypes = ['application/json'];
      var accepts = ['application/json'];
      var returnType = [MemeInfo];

      return this.apiClient.callApi(
        '/meme', 'GET',
        pathParams, queryParams, collectionQueryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, callback
      );
    }

    /**
     * Callback function to receive the result of the memeMemeIdDelete operation.
     * @callback module:api/DefaultApi~memeMemeIdDeleteCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete meme by ID
     * Remove a meme.
     * @param {Number} memeId ID of meme to remove
     * @param {module:api/DefaultApi~memeMemeIdDeleteCallback} callback The callback function, accepting three arguments: error, data, response
     */
    this.memeMemeIdDelete = function(memeId, callback) {
      var postBody = null;

      // verify the required parameter 'memeId' is set
      if (memeId === undefined || memeId === null) {
        throw new Error("Missing the required parameter 'memeId' when calling memeMemeIdDelete");
      }


      var pathParams = {
        'meme-id': memeId
      };
      var queryParams = {
      };
      var collectionQueryParams = {
      };
      var headerParams = {
      };
      var formParams = {
      };

      var authNames = ['oauthFacebook'];
      var contentTypes = ['application/json'];
      var accepts = ['application/json'];
      var returnType = null;

      return this.apiClient.callApi(
        '/meme/{meme-id}', 'DELETE',
        pathParams, queryParams, collectionQueryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, callback
      );
    }

    /**
     * Callback function to receive the result of the memeMemeIdGet operation.
     * @callback module:api/DefaultApi~memeMemeIdGetCallback
     * @param {String} error Error message, if any.
     * @param {File} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get meme by ID
     * Return a meme.
     * @param {Number} memeId ID of meme to return
     * @param {module:api/DefaultApi~memeMemeIdGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link File}
     */
    this.memeMemeIdGet = function(memeId, callback) {
      var postBody = null;

      // verify the required parameter 'memeId' is set
      if (memeId === undefined || memeId === null) {
        throw new Error("Missing the required parameter 'memeId' when calling memeMemeIdGet");
      }


      var pathParams = {
        'meme-id': memeId
      };
      var queryParams = {
      };
      var collectionQueryParams = {
      };
      var headerParams = {
      };
      var formParams = {
      };

      var authNames = ['oauthFacebook'];
      var contentTypes = ['application/json'];
      var accepts = ['application/json'];
      var returnType = File;

      return this.apiClient.callApi(
        '/meme/{meme-id}', 'GET',
        pathParams, queryParams, collectionQueryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, callback
      );
    }

    /**
     * Callback function to receive the result of the memePost operation.
     * @callback module:api/DefaultApi~memePostCallback
     * @param {String} error Error message, if any.
     * @param {File} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Post meme
     * Create a meme.
     * @param {String} topcaption Top caption for meme (URL-encoded string)
     * @param {String} bottomcaption Bottom caption for meme (URL-encoded string)
     * @param {File} image Background image for meme
     * @param {module:api/DefaultApi~memePostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link File}
     */
    this.memePost = function(topcaption, bottomcaption, image, callback) {
      var postBody = null;

      // verify the required parameter 'topcaption' is set
      if (topcaption === undefined || topcaption === null) {
        throw new Error("Missing the required parameter 'topcaption' when calling memePost");
      }

      // verify the required parameter 'bottomcaption' is set
      if (bottomcaption === undefined || bottomcaption === null) {
        throw new Error("Missing the required parameter 'bottomcaption' when calling memePost");
      }

      // verify the required parameter 'image' is set
      if (image === undefined || image === null) {
        throw new Error("Missing the required parameter 'image' when calling memePost");
      }


      var pathParams = {
      };
      var queryParams = {
        'topcaption': topcaption,
        'bottomcaption': bottomcaption,
      };
      var collectionQueryParams = {
      };
      var headerParams = {
      };
      var formParams = {
        'image': image
      };

      var authNames = ['oauthFacebook'];
      var contentTypes = ['image/jpeg', 'image/gif', 'image/png', 'multipart/form-data'];
      var accepts = ['image/jpeg'];
      var returnType = File;

      return this.apiClient.callApi(
        '/meme', 'POST',
        pathParams, queryParams, collectionQueryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, callback
      );
    }
  };

  return exports;
}));
