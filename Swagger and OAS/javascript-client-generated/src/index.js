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

(function(factory) {
  if (typeof define === 'function' && define.amd) {
    // AMD. Register as an anonymous module.
    define(['ApiClient', 'model/Error', 'model/ErrorLogData', 'model/NewPlaylist', 'model/PlaylistWithSongs', 'model/Song', 'api/DefaultApi'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    module.exports = factory(require('./ApiClient'), require('./model/Error'), require('./model/ErrorLogData'), require('./model/NewPlaylist'), require('./model/PlaylistWithSongs'), require('./model/Song'), require('./api/DefaultApi'));
  }
}(function(ApiClient, Error, ErrorLogData, NewPlaylist, PlaylistWithSongs, Song, DefaultApi) {
  'use strict';

  /**
   * Music_API_with_playlists.<br>
   * The <code>index</code> module provides access to constructors for all the classes which comprise the public API.
   * <p>
   * An AMD (recommended!) or CommonJS application will generally do something equivalent to the following:
   * <pre>
   * var MusicApi = require('index'); // See note below*.
   * var xxxSvc = new MusicApi.XxxApi(); // Allocate the API class we're going to use.
   * var yyyModel = new MusicApi.Yyy(); // Construct a model instance.
   * yyyModel.someProperty = 'someValue';
   * ...
   * var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
   * ...
   * </pre>
   * <em>*NOTE: For a top-level AMD script, use require(['index'], function(){...})
   * and put the application logic within the callback function.</em>
   * </p>
   * <p>
   * A non-AMD browser application (discouraged) might do something like this:
   * <pre>
   * var xxxSvc = new MusicApi.XxxApi(); // Allocate the API class we're going to use.
   * var yyy = new MusicApi.Yyy(); // Construct a model instance.
   * yyyModel.someProperty = 'someValue';
   * ...
   * var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
   * ...
   * </pre>
   * </p>
   * @module index
   * @version 0.3.0
   */
  var exports = {
    /**
     * The ApiClient constructor.
     * @property {module:ApiClient}
     */
    ApiClient: ApiClient,
    /**
     * The Error model constructor.
     * @property {module:model/Error}
     */
    Error: Error,
    /**
     * The ErrorLogData model constructor.
     * @property {module:model/ErrorLogData}
     */
    ErrorLogData: ErrorLogData,
    /**
     * The NewPlaylist model constructor.
     * @property {module:model/NewPlaylist}
     */
    NewPlaylist: NewPlaylist,
    /**
     * The PlaylistWithSongs model constructor.
     * @property {module:model/PlaylistWithSongs}
     */
    PlaylistWithSongs: PlaylistWithSongs,
    /**
     * The Song model constructor.
     * @property {module:model/Song}
     */
    Song: Song,
    /**
     * The DefaultApi service constructor.
     * @property {module:api/DefaultApi}
     */
    DefaultApi: DefaultApi
  };

  return exports;
}));