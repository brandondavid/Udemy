# coding: utf-8

"""
    Music API

    **Music API with playlists**  # noqa: E501

    OpenAPI spec version: 0.3.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class DefaultApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_playlist_id(self, playlist_id, **kwargs):  # noqa: E501
        """delete_playlist_id  # noqa: E501

        **Remove a playlist.**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_playlist_id(playlist_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str playlist_id: ID of the playlist to remove (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_playlist_id_with_http_info(playlist_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_playlist_id_with_http_info(playlist_id, **kwargs)  # noqa: E501
            return data

    def delete_playlist_id_with_http_info(self, playlist_id, **kwargs):  # noqa: E501
        """delete_playlist_id  # noqa: E501

        **Remove a playlist.**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_playlist_id_with_http_info(playlist_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str playlist_id: ID of the playlist to remove (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['playlist_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_playlist_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'playlist_id' is set
        if ('playlist_id' not in params or
                params['playlist_id'] is None):
            raise ValueError("Missing the required parameter `playlist_id` when calling `delete_playlist_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'playlist_id' in params:
            path_params['playlist-id'] = params['playlist_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/playlist/{playlist-id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_image(self, playlist_id, **kwargs):  # noqa: E501
        """get_image  # noqa: E501

        **Returns a generated image for the playlist.**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_image(playlist_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str playlist_id: ID of the playlist for which to generate an image (required)
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_image_with_http_info(playlist_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_image_with_http_info(playlist_id, **kwargs)  # noqa: E501
            return data

    def get_image_with_http_info(self, playlist_id, **kwargs):  # noqa: E501
        """get_image  # noqa: E501

        **Returns a generated image for the playlist.**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_image_with_http_info(playlist_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str playlist_id: ID of the playlist for which to generate an image (required)
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['playlist_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_image" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'playlist_id' is set
        if ('playlist_id' not in params or
                params['playlist_id'] is None):
            raise ValueError("Missing the required parameter `playlist_id` when calling `get_image`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'playlist_id' in params:
            path_params['playlist-id'] = params['playlist_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['image/png'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/playlist/{playlist-id}/image', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_playlist(self, **kwargs):  # noqa: E501
        """get_playlist  # noqa: E501

        **Return one or more playlists.**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_playlist(async=True)
        >>> result = thread.get()

        :param async bool
        :param int limit: Number of playlists to return
        :param int offset: Number of playlists to skip
        :param str search: Search term
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_playlist_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_playlist_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_playlist_with_http_info(self, **kwargs):  # noqa: E501
        """get_playlist  # noqa: E501

        **Return one or more playlists.**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_playlist_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param int limit: Number of playlists to return
        :param int offset: Number of playlists to skip
        :param str search: Search term
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['limit', 'offset', 'search']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_playlist" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'search' in params:
            query_params.append(('search', params['search']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/playlist', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_playlist_id(self, playlist_id, **kwargs):  # noqa: E501
        """get_playlist_id  # noqa: E501

        **Return a playlist.**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_playlist_id(playlist_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str playlist_id: ID of the playlist to return (required)
        :return: PlaylistWithSongs
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_playlist_id_with_http_info(playlist_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_playlist_id_with_http_info(playlist_id, **kwargs)  # noqa: E501
            return data

    def get_playlist_id_with_http_info(self, playlist_id, **kwargs):  # noqa: E501
        """get_playlist_id  # noqa: E501

        **Return a playlist.**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_playlist_id_with_http_info(playlist_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str playlist_id: ID of the playlist to return (required)
        :return: PlaylistWithSongs
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['playlist_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_playlist_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'playlist_id' is set
        if ('playlist_id' not in params or
                params['playlist_id'] is None):
            raise ValueError("Missing the required parameter `playlist_id` when calling `get_playlist_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'playlist_id' in params:
            path_params['playlist-id'] = params['playlist_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/playlist/{playlist-id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PlaylistWithSongs',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_playlist(self, new_playlist, **kwargs):  # noqa: E501
        """post_playlist  # noqa: E501

        **Create a new playlist.**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.post_playlist(new_playlist, async=True)
        >>> result = thread.get()

        :param async bool
        :param NewPlaylist new_playlist: The playlist to create (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.post_playlist_with_http_info(new_playlist, **kwargs)  # noqa: E501
        else:
            (data) = self.post_playlist_with_http_info(new_playlist, **kwargs)  # noqa: E501
            return data

    def post_playlist_with_http_info(self, new_playlist, **kwargs):  # noqa: E501
        """post_playlist  # noqa: E501

        **Create a new playlist.**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.post_playlist_with_http_info(new_playlist, async=True)
        >>> result = thread.get()

        :param async bool
        :param NewPlaylist new_playlist: The playlist to create (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['new_playlist']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_playlist" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'new_playlist' is set
        if ('new_playlist' not in params or
                params['new_playlist'] is None):
            raise ValueError("Missing the required parameter `new_playlist` when calling `post_playlist`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'new_playlist' in params:
            body_params = params['new_playlist']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/playlist', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
