# coding: utf-8

"""
    Meme Meister

    API to create memes  # noqa: E501

    OpenAPI spec version: 0.1.0
    
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

    def meme_get(self, **kwargs):  # noqa: E501
        """Get meme(s)  # noqa: E501

        Returns one or more memes  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.meme_get(async=True)
        >>> result = thread.get()

        :param async bool
        :param str q: Optional URL-encoded search term
        :return: list[MemeInfo]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.meme_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.meme_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def meme_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get meme(s)  # noqa: E501

        Returns one or more memes  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.meme_get_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str q: Optional URL-encoded search term
        :return: list[MemeInfo]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['q']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method meme_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'q' in params:
            query_params.append(('q', params['q']))  # noqa: E501

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
        auth_settings = ['oauthFacebook']  # noqa: E501

        return self.api_client.call_api(
            '/meme', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[MemeInfo]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def meme_meme_id_delete(self, meme_id, **kwargs):  # noqa: E501
        """Delete meme by ID  # noqa: E501

        Remove a meme.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.meme_meme_id_delete(meme_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int meme_id: ID of meme to remove (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.meme_meme_id_delete_with_http_info(meme_id, **kwargs)  # noqa: E501
        else:
            (data) = self.meme_meme_id_delete_with_http_info(meme_id, **kwargs)  # noqa: E501
            return data

    def meme_meme_id_delete_with_http_info(self, meme_id, **kwargs):  # noqa: E501
        """Delete meme by ID  # noqa: E501

        Remove a meme.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.meme_meme_id_delete_with_http_info(meme_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int meme_id: ID of meme to remove (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['meme_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method meme_meme_id_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'meme_id' is set
        if ('meme_id' not in params or
                params['meme_id'] is None):
            raise ValueError("Missing the required parameter `meme_id` when calling `meme_meme_id_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'meme_id' in params:
            path_params['meme-id'] = params['meme_id']  # noqa: E501

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
        auth_settings = ['oauthFacebook']  # noqa: E501

        return self.api_client.call_api(
            '/meme/{meme-id}', 'DELETE',
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

    def meme_meme_id_get(self, meme_id, **kwargs):  # noqa: E501
        """Get meme by ID  # noqa: E501

        Return a meme.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.meme_meme_id_get(meme_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int meme_id: ID of meme to return (required)
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.meme_meme_id_get_with_http_info(meme_id, **kwargs)  # noqa: E501
        else:
            (data) = self.meme_meme_id_get_with_http_info(meme_id, **kwargs)  # noqa: E501
            return data

    def meme_meme_id_get_with_http_info(self, meme_id, **kwargs):  # noqa: E501
        """Get meme by ID  # noqa: E501

        Return a meme.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.meme_meme_id_get_with_http_info(meme_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int meme_id: ID of meme to return (required)
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['meme_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method meme_meme_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'meme_id' is set
        if ('meme_id' not in params or
                params['meme_id'] is None):
            raise ValueError("Missing the required parameter `meme_id` when calling `meme_meme_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'meme_id' in params:
            path_params['meme-id'] = params['meme_id']  # noqa: E501

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
        auth_settings = ['oauthFacebook']  # noqa: E501

        return self.api_client.call_api(
            '/meme/{meme-id}', 'GET',
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

    def meme_post(self, topcaption, bottomcaption, image, **kwargs):  # noqa: E501
        """Post meme  # noqa: E501

        Create a meme.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.meme_post(topcaption, bottomcaption, image, async=True)
        >>> result = thread.get()

        :param async bool
        :param str topcaption: Top caption for meme (URL-encoded string) (required)
        :param str bottomcaption: Bottom caption for meme (URL-encoded string) (required)
        :param file image: Background image for meme (required)
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.meme_post_with_http_info(topcaption, bottomcaption, image, **kwargs)  # noqa: E501
        else:
            (data) = self.meme_post_with_http_info(topcaption, bottomcaption, image, **kwargs)  # noqa: E501
            return data

    def meme_post_with_http_info(self, topcaption, bottomcaption, image, **kwargs):  # noqa: E501
        """Post meme  # noqa: E501

        Create a meme.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.meme_post_with_http_info(topcaption, bottomcaption, image, async=True)
        >>> result = thread.get()

        :param async bool
        :param str topcaption: Top caption for meme (URL-encoded string) (required)
        :param str bottomcaption: Bottom caption for meme (URL-encoded string) (required)
        :param file image: Background image for meme (required)
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['topcaption', 'bottomcaption', 'image']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method meme_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'topcaption' is set
        if ('topcaption' not in params or
                params['topcaption'] is None):
            raise ValueError("Missing the required parameter `topcaption` when calling `meme_post`")  # noqa: E501
        # verify the required parameter 'bottomcaption' is set
        if ('bottomcaption' not in params or
                params['bottomcaption'] is None):
            raise ValueError("Missing the required parameter `bottomcaption` when calling `meme_post`")  # noqa: E501
        # verify the required parameter 'image' is set
        if ('image' not in params or
                params['image'] is None):
            raise ValueError("Missing the required parameter `image` when calling `meme_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'topcaption' in params:
            query_params.append(('topcaption', params['topcaption']))  # noqa: E501
        if 'bottomcaption' in params:
            query_params.append(('bottomcaption', params['bottomcaption']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'image' in params:
            local_var_files['image'] = params['image']  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['image/jpeg'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['image/jpeg', 'image/gif', 'image/png', 'multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauthFacebook']  # noqa: E501

        return self.api_client.call_api(
            '/meme', 'POST',
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
