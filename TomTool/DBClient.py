#!/usr/bin/env python
# -*- coding: utf-8 -*-

import psycopg2


def detuple(tup):
    """
    Forces a singleton tuple to a plain value.
    Returns everything else unchanged.
    """
    return tup[0] if isinstance(tup, tuple) and len(tup) == 1 else tup


class DBClient(object):
    """
    Generic wrapper around a psycopg2 database connection
    to run a query and get the results.
    """
    def __init__(self, db, user, host, port, password):
        connection_parameters = u"dbname='{}' user='{}' host='{}' port={} password='{}'".format(
            db,user,host,port,password)
        self._connection = psycopg2.connect(connection_parameters)

    def close(self):
        self._connection.close()

    def _fetchall(self, query):
        """
        Runs a query and returns all the results.
        """
        with self._connection as conn:
            with conn.cursor() as cur:
                cur.execute(query)
                return map(detuple, cur.fetchall())

    def _fetchone(self, query):
        """
        Runs a query and returns the first result.
        """
        with self._connection as conn:
            with conn.cursor() as cur:
                cur.execute(query)
                row = cur.fetchone()
                return detuple(row)


class Test3Client(DBClient):

    def __init__(self):
        super(Test3Client, self).__init__(
            db='test3', user='wasplab',
            host='localhost', port=9100,
            password='wasplab')

    def send_query_activeIncubated(self, mode):

        query = "SELECT media_barcode from media where active=TRUE and status='INCUBATED'"
        if mode in (1, 2, 3):  # Select a single incubator
            query += " and position={}".format(mode)
        elif mode == 0:
            pass
        else:
            raise ValueError("Unknown mode {}".format(mode))

        return self._fetchall(query)

    def send_query_mediaInfo(self, barcode):
        query = "SELECT * from media where media_barcode = '{}' and active = (true)".format(barcode)
        return self._fetchone(query)

    def send_query_statusInc(self):

        query = "SELECT id,active from incubator where id<999"
        data = self._fetchall(query)
        data = sorted(data, key=lambda inc: inc[0])

        return data


class ActivitiClient(DBClient):

    def __init__(self):
        super(ActivitiClient, self).__init__(
            db='activiti', user='wasplab',
            host='localhost', port=9100,
            password='wasplab')

    def send_query_user(self):
        return self._fetchall("SELECT * from act_id_user")
