#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# @Time : 2021/5/18 12:12
# @Author : russell
# @File :  testClick



import click
from pyartifactory import Artifactory
from pyartifactory.models import LocalRepository, VirtualRepository, RemoteRepository
from pprint import pprint


def read_config(file:str):
    return dict(url="http://10.10.7.25:8081/artifactory", auth=('admin', 'password'), verify=False, api_version=1)



@click.group('cli')
@click.option('--file','-f',type=str,help='config file')
@click.pass_context
def cli(ctx,file):
    ctx.obj={}
    conf=read_config(file)
    ctx.obj = {
        'arti': Artifactory(**conf),
        'file':file,
    }



@click.group('repo')
@click.pass_context
def repo(ctx):
    pass



@repo.command('create', short_help='create repo')
@click.option('--name', help='repo to create')
@click.argument('name')
@click.pass_context
def create(ctx,name):
    """
    create [repo name]
    """
    arti=ctx.obj['arti']
    try:
        new=arti.repositories.create_repo(LocalRepository(key=name))
        if new:
            print('success')
            pprint(new,depth=1)
    except Exception as e:
        click.echo(e)



@repo.command('delete', short_help='delete repo')
@click.option('--name', help='repo to delete')
@click.argument('name')
@click.pass_context
def delete(ctx,name):
    """
    delete [repo name]
    """
    arti=ctx.obj['arti']
    try:
        result=arti.repositories.delete(name)
        print('success')
    except Exception as e:
        click.echo(e)

@repo.command('info', short_help='info repo')
@click.option('--name', help='info repo')
@click.argument('name')
@click.pass_context
def info(ctx,name):
    """
    info [repo name]
    """
    arti=ctx.obj['arti']
    pprint(arti.artifacts.info(name),depth=1)


@repo.command('list', short_help='list repo')
@click.pass_context
def list(ctx):
    """
    list all repo
    """
    arti=ctx.obj['arti']
    pprint(arti.repositories.list(),depth=1)





@click.group('artifact')
@click.pass_context
def artifact(ctx):
    pass


@artifact.command('deploy')
@click.option('--local', type=str,help='local file path')
@click.option('--artifact', type=str,help='remote artifact file path')
@click.argument('local')
@click.argument('artifact')
@click.pass_context
def deploy(ctx,local, artifact):
    """
    deploy [local_file] [repo_dir_file_name]

    deploy --local [local_file] --artifact [repo_dir_file_name]
    """
    print(local,artifact)
    arti = ctx.obj['arti']
    try:
        result=arti.artifacts.deploy(local, artifact)
        click.echo('success')
        pprint(result, depth = 1)
    except Exception as e:
        click.echo(e)


@artifact.command('copy')
@click.option('--source', help='source artifact file path')
@click.option('--destination', help='destination artifact file path')
@click.argument('source')
@click.argument('destination')
@click.pass_context
def copy(ctx,source,destination):
    """
    copy [repo_dir_file_name] [repo_dir_file_name]

    move --src [repo_dir_file_name] --des [repo_dir_file_name]
    """
    arti = ctx.obj['arti']
    try:
        result=arti.artifacts.copy(source, destination)
        click.echo('success')
        pprint(result, depth = 1)
    except Exception as e:
        click.echo(e)



@artifact.command('download')
@click.option('--artifact', help='artifact file path')
@click.option('--local', help='local dir path')
@click.argument('artifact')
@click.argument('local')
@click.pass_context
def download(ctx,artifact,local):
    """
    download [repo_dir_file_name] [local_dir]

    download --artifact [repo_dir_file_name]  --local [local_dir]
    """
    arti = ctx.obj['arti']
    try:
        result=arti.artifacts.download(artifact, local)
        click.echo('success')
        pprint(result, depth = 1)
    except Exception as e:
        click.echo(e)


@artifact.command('delete')
@click.option('--artifact', help='artifact file path')
@click.argument('artifact')
@click.pass_context
def delete(ctx,artifact):
    """
    delete [repo_dir_file_name]
    delete --artifact [repo_dir_file_name]
    """
    arti = ctx.obj['arti']
    try:
        result=arti.artifacts.delete(artifact)
        click.echo('success')
        pprint(result, depth = 1)
    except Exception as e:
        click.echo(e)



@artifact.command('move')
@click.option('--source', help='source artifact file path')
@click.option('--destination', help='destination artifact file path')
@click.argument('source')
@click.argument('destination')
@click.pass_context
def move(ctx,source,destination):
    """
    move [repo_dir_file_name] [repo_dir_file_name]

    move --src [repo_dir_file_name] --des [repo_dir_file_name]
    """
    arti = ctx.obj['arti']
    try:
        result=arti.artifacts.move(source, destination)
        click.echo('success')
        pprint(result, depth = 1)
    except Exception as e:
        click.echo(e)





cli.add_command(repo)
cli.add_command(artifact)



if __name__ == '__main__':
    cli(obj={})
